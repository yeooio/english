import csv, collections, re

rows = list(csv.reader(open('results/模型对比表汇总.csv', encoding='utf-8')))[1:]
g = collections.defaultdict(dict)
for r in rows:
    g[(r[0], r[1])][r[2]] = {'R2': float(r[3]), 'MAE': float(r[5]),
                             'MAPE': float(r[6]) / 100, 'RMSE': float(r[4])}

name = {'MS-AgentNet': 'MS_AgentNet', 'CNN-Transformer': 'CNN_Transformer',
        'CNN-LSTM': 'CNN_LSTM', 'Transformer': 'Transformer', 'LSTM': 'LSTM'}
order = ['MS-AgentNet', 'CNN-Transformer', 'CNN-LSTM', 'Transformer', 'LSTM']
num_re = re.compile(r'^(?:\\textbf\{)?([0-9]+\.[0-9]+)\}?$')


def parse(path):
    out = []
    for line in open(path, encoding='utf-8'):
        body = line.rstrip().rstrip('\\')
        parts = [p.strip() for p in body.split('&')]
        if len(parts) != 6 or parts[1] not in name:
            continue
        nums = []
        for p in parts[2:]:
            m = num_re.match(p)
            if not m:
                nums = None
                break
            nums.append(float(m.group(1)))
        if nums:
            out.append((parts[1], nums))
    return out


def check(path, cells):
    data = parse(path)
    expected = 5 * (len(cells) + 1)
    print(path, 'parsed rows =', len(data), 'expected =', expected)
    assert len(data) == expected
    bad = 0
    keys = ['R2', 'MAE', 'MAPE', 'RMSE']
    for gi, ck in enumerate(cells + ['AVG']):
        for j, m in enumerate(order):
            mm, nums = data[gi * 5 + j]
            assert mm == m, (ck, mm, m)
            if ck == 'AVG':
                ref = {k: sum(g[c][name[m]][k] for c in cells) / len(cells) for k in keys}
            else:
                ref = g[ck][name[m]]
            for k, v in zip(keys, nums):
                if abs(v - round(ref[k], 5)) > 1e-9:
                    print('  MISMATCH', ck, m, k, v, round(ref[k], 5))
                    bad += 1
    print('  mismatches =', bad)


ox = [('oxford', 'cell%d' % i) for i in range(2, 9)]
six = [('cs', 'cs37'), ('cs', 'cs38'), ('cx', 'cx37'), ('cx', 'cx38'),
       ('mit', 'mit_c13'), ('mit', 'mit_c29')]
check('tables/table_4_5.tex', ox)
check('tables/table_4_6.tex', six)
