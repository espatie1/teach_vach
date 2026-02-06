from itertools import product

alphabet = ['А', 'К', 'Р', 'У', 'Ч']
valid_count = 0
last_valid_index = 0
index = 0

for word in product(alphabet, repeat=5):
    index += 1
    s = ''.join(word)
    if s.count('Ч') <= 1 and 'УУ' not in s:
        last_valid_index = index

print(last_valid_index)
