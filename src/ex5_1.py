def f(n):
    y=bin(n)[2:]
    if n%2==0:
        y = y.replace('1','11')        
    if n%2==1:
        y = y.replace('0','00')
    return int(y,2)#перевод 2 записи  в 10-ые числа
print(f(5))
for N in range(1000):
    result=f(N)
    if result >70:
        print(N)
        break