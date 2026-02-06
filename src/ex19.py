def igra(kucha, chod):
    if kucha >= 229:
        return chod == 2 or chod == 4
    if chod % 2 == 1:
        return all([igra(int(kucha + 1), chod + 1), igra(int(kucha * 2), chod + 1)])
    else:
        return any([igra(int(kucha + 1), chod + 1), igra(int(kucha * 2), chod + 1)])
    
for kamni in range (1, 229):
    if igra(kamni, 0) == True:
        print(kamni)