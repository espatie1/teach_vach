MAX = 0

def chetverch(num) -> str:
    chetver= []
    while num > 4:
        result = num % 4
        chetver.append(str(result))
        num = num // 4
    if num > 0:
        chetver.append(str(num))
    result2 = "".join(reversed(chetver))
    return result2

def desiatok(num):
    stepen = 0
    cislo = num[::-1]
    result = 0
    for cifra in cislo:
        result += int(cifra) * 4**stepen
        stepen = stepen + 1
    return result

for N in range (0, 1000):
    N = 11
    N4 = chetverch(N)
    if N % 4 == 0:
        N4= N4 + N4[-2:]
    else: 
        ostatok = (N % 4) * 2
        ostatok4 = chetverch(ostatok)
        N4 = N4 + ostatok4
    if (desiatok(N4) < 261):
        MAX = N
    print(desiatok(N4))
    
    
   
   
 