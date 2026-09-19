from pathlib import Path
import re
import statistics
import json

root = Path('D:/MS-AgentNet-English')
specs = {
    'Engineering-AI': ('To address the computational bottleneck', '1. Introduction'),
    'BMSFormer': ('The efficient and accurate', 'Keywords:'),
    'JESSOHRUL': ('Accurate assessment', '1. Introduction'),
}
result = {}
for paper, (start, end) in specs.items():
    raw = (root/'style-references'/paper/'abstract.txt').read_text(encoding='utf-8')
    passage = start + raw.split(start, 1)[1].split(end, 1)[0]
    passage = re.sub(r'\u00ad\s*', '', passage)
    passage = re.sub(r'\s+', ' ', passage).strip()
    passage = passage.replace('Local– Global', 'Local–Global')
    passage = passage.replace('state-ofthe-art', 'state-of-the-art')
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', passage)
    counts = [len(s.split()) for s in sentences]
    result[paper] = {'sentence_count':len(sentences), 'word_count':sum(counts),
                     'min':min(counts), 'median':statistics.median(counts), 'max':max(counts),
                     'sentences':[{'id':i+1, 'words':c, 'start':' '.join(s.split()[:6])}
                                  for i,(s,c) in enumerate(zip(sentences,counts))]}
dest = root/'tmp'/'grammar-reference-measurement.json'
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
