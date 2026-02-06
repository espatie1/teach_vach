goal = 3
start = 24
cislo_v = 
cislo_ne = 14

kolvo_puti = 0
def ways(n, list):
    global kolvo_puti
    if n == goal:
        if cislo_v in list:
            if not(cislo_ne in list):
                kolvo_puti += 1
    if goal > start:
        if n > goal:
            return
    else:
        if n < goal:
            return
    ways(n+1, list | {n+1})
    ways(n*2, list | {n*2})
    ways(n*3, list | {n*3})

ways(start, {start})
print(kolvo_puti)