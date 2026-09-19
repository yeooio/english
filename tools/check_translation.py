"""Conservative source/translation comparison; standard library only.

Reports differences for human review. Not a TeX parser or language-quality judge.
Exit 0: no reported differences; 1: review required; 2: input/configuration error.
Optional glossary JSON: [{"preferred": "health indicator", "flag_variants":
["health index"]}]. Only include confirmed conflicts; no automatic replacement.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


def uncomment(text):
    lines = []
    for line in text.splitlines():
        cut = len(line)
        for i, char in enumerate(line):
            if char == '%':
                j = i - 1
                while j >= 0 and line[j] == '\\':
                    j -= 1
                if (i - j - 1) % 2 == 0:
                    cut = i
                    break
        lines.append(line[:cut])
    return '\n'.join(lines)


def braced(text, start):
    depth = 0
    for i in range(start, len(text)):
        if text[i] in '{}':
            j = i - 1
            while j >= 0 and text[j] == '\\':
                j -= 1
            if (i - j - 1) % 2:
                continue
            depth += 1 if text[i] == '{' else -1
            if depth == 0:
                return text[start + 1:i]
    raise ValueError('unclosed protected argument')


def protected(text):
    values = []
    pattern = r'\\(label|(?:[cC]ref|[cC]pageref|ref|eqref|pageref)|[A-Za-z]*cite[A-Za-z]*|input|include|includegraphics|bibitem|url|href)\*?\s*(?:\[[^\]]*\]\s*)*\{'
    for match in re.finditer(pattern, text):
        values.append((match[1], braced(text, match.end() - 1)))
    return Counter(values)


def mathematics(text):
    # Common math forms; uncommon/custom environments require manual review.
    pattern = r'(?s)\\begin\{(?P<env>equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?|displaymath|math)\}.*?\\end\{(?P=env)\}|\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$(?!\$).*?(?<!\\)\$'
    return Counter(re.sub(r'\s+', '', m[0]) for m in re.finditer(pattern, text))


def compare(source, target):
    a, b = uncomment(source), uncomment(target)
    findings = []
    checks = {
        'protected arguments': protected,
        'math blocks (whitespace normalized)': mathematics,
        'command counts': lambda s: Counter(re.findall(r'\\[A-Za-z]+\*?', s)),
        'environment sequence': lambda s: re.findall(r'\\(?:begin|end)\{[^}]+\}', s),
        'numeric tokens': lambda s: Counter(re.findall(r'(?<![\w])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?', s)),
    }
    for name, extract in checks.items():
        left, right = extract(a), extract(b)
        if left != right:
            if isinstance(left, Counter):
                findings.append({'check': name, 'removed': list((left - right).elements()),
                                 'added': list((right - left).elements())})
            else:
                findings.append({'check': name, 'source': left, 'target': right})
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('target', type=Path)
    parser.add_argument('--glossary', type=Path)
    parser.add_argument('--final', action='store_true', help='flag remaining Chinese in target')
    args = parser.parse_args()
    try:
        source = args.source.read_text(encoding='utf-8-sig')
        target = args.target.read_text(encoding='utf-8-sig')
        findings = compare(source, target)
        visible = uncomment(target)
        if args.glossary:
            entries = json.loads(args.glossary.read_text(encoding='utf-8-sig'))
            if not isinstance(entries, list):
                raise ValueError('glossary must be a list')
            for entry in entries:
                preferred = entry['preferred']
                variants = entry.get('flag_variants', [])
                if not isinstance(preferred, str) or not isinstance(variants, list):
                    raise ValueError('invalid glossary entry')
                for variant in variants:
                    if not isinstance(variant, str) or not variant.strip():
                        raise ValueError('glossary variant must be a nonempty string')
                    for m in re.finditer(r'(?<!\w)' + re.escape(variant) + r'(?!\w)', visible, re.I):
                        findings.append({'check': 'terminology candidate', 'found': m[0],
                                         'preferred': preferred, 'line': visible.count('\n', 0, m.start()) + 1})
        if args.final:
            for n, line in enumerate(visible.splitlines(), 1):
                if re.search(r'[\u3400-\u9fff]', line):
                    findings.append({'check': 'remaining Chinese', 'line': n, 'text': line})
        print(json.dumps({'status': 'REVIEW' if findings else 'PASS', 'findings': findings,
                          'limits': 'Checks common TeX forms, not all macros. Numeric differences may be legitimate. Units, prose meaning, grammar, image text and context-sensitive terminology require human review.'}, ensure_ascii=False, indent=2))
        return 1 if findings else 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
