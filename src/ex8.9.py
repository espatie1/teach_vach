from itertools import product
alvavit=list('А' 'В' 'И' 'О' 'Р' 'Т' 'Ф')
chetchik=0
s=1
for slovo in product(alvavit, repeat=6):
    q=''.join(slovo)
    if (s % 2 == 0) and (q[0] != 'О') and (q.count('Р') == 2):
        chetchik = chetchik + 1
    s=s+1
print(chetchik)