def DEL(n, m):
    if n % m == 0:
        return True
    else:
        return False
MAXIMUM = 0
for A in range(1, 1000):
    net_oshibok = True
    for x in range(1, 1000):
        #(not DEL(x, A)) <= (DEL(x, 54) <= (not DEL(162, x)))
        if (DEL(x,A) or ((not DEL(x, 54)) or (not DEL(162, x)))) == 0:
            net_oshibok = False
            break
    if net_oshibok == True:
        MAXIMUM = A
print(MAXIMUM)