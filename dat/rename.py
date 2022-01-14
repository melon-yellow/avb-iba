
import os

prefix = 'H:/iba_dat/2019/'

elist = [f for f in os.listdir(prefix) if not os.path.isfile(os.path.join(prefix, f))]

for el in elist:
    if '2019' not in el: continue
    src = prefix + el
    dst = prefix + el.replace('2019', '19')
    os.rename(src, dst)
