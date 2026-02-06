print('    w x y z')
for w in [0, 1]:
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                F = x and (y <= z) and ((not y) <= ((not z) == w))
                if (x+y+z+w >= 3) and (F == 0):
                    print('3: ', w, x, y, z )
                if (x+y+z+w == 2) and (F == 1):
                    print('1: ', w, x, y, z )