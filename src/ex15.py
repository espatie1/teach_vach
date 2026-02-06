def DEL(n, m):
    if (n % m == 0):
        return True
    else:
        return False
    
for A in range(1, 400):
    k = True
    for x in range (1, 400):
        if ((DEL(x, 14) <= (not(DEL(x,4)))) or ((x + A) >= 200)) == False :
            k = False
    if (k == True):
        print(A)
        break

