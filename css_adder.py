import os, re

directory = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(directory)

for htmls in files:
    if htmls.endswith('.html'):
        with open(htmls, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        with open(htmls, 'w', encoding='utf-8') as f:
            for line in lines:
                if re.search('<head>', line):
                    f.write('<link rel="stylesheet" href="style.css">')
                f.write(line)
