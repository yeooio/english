import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('checker', Path(__file__).with_name('check_translation.py'))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class Checks(unittest.TestCase):
    def test_translation_and_visible_argument(self):
        self.assertEqual(checker.compare(r'\textbf{结果}为 $x=2$，见\cref{fig:a}。',
                                         r'\textbf{The result} is $x = 2$; see \cref{fig:a}.'), [])

    def test_changed_key_same_command_count(self):
        result = checker.compare(r'\cite{ref1}', r'\cite{ref2}')
        self.assertIn('protected arguments', [x['check'] for x in result])

    def test_changed_math_same_digits(self):
        result = checker.compare(r'$x+y=2$', r'$x-y=2$')
        self.assertIn('math blocks (whitespace normalized)', [x['check'] for x in result])

    def test_added_command(self):
        result = checker.compare('Text', r'\emph{Text}')
        self.assertIn('command counts', [x['check'] for x in result])

    def test_changed_number(self):
        self.assertTrue(checker.compare('误差0.12', 'Error 0.21'))

    def test_comments_and_escaped_percent(self):
        self.assertEqual(checker.uncomment('a\\% b % comment'), 'a\\% b ')

    def test_unclosed_argument(self):
        with self.assertRaises(ValueError):
            checker.compare(r'\ref{a}', r'\ref{a')

    def test_nested_protected_path(self):
        self.assertEqual(checker.protected(r'\input{dir/{name}.tex}'),
                         {('input', 'dir/{name}.tex'): 1})


if __name__ == '__main__':
    unittest.main()
