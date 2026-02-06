R_min = 1000000
for N in range(20, 100):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = "11" + R
        R = R[:-1] + "1"
        print(R)
    else:
        R = "10" + R
        R = R[:-1] + "0"
        print(R)
    R = int(R, 2)
    R_min = min(R, R_min)
    if R < R_min:
        R_min = R


print(N, R_min)