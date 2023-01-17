import os

directory = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(directory)

for htmls in files:
    if htmls.endswith('.html'):
        with open(htmls, 'rt', encoding='utf-8') as f:
            x = f.read()
        with open(htmls, 'wt', encoding='utf-8') as f:
            x = x.replace('index.php?title=', 'dakapo_wiki/')
            f.write(x)

