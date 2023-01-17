import requests
import numpy as np

fname='dakapo.txt'
dakapo = 'https://dakapo.wiki/index.php?title='
names = np.loadtxt(fname, encoding='utf-8', dtype=str)

for name in names:
    url = dakapo + name
    page = name + '.html'
    r = requests.get(url)
    html_file = open(page, 'w', encoding='utf-8')
    html_file.write(r.text)
    html_file.close()
