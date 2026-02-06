for N in range (0,1000):
    h = bin(N)[2:]
    if N%2 == 0:
        result = h.replace('1','11')
    else:
        result = h.replace('0','00')
    R= int(result, 2)
    if R > 70:
        print (N)
        break