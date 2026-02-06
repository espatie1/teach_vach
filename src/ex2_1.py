print("x y z w")
for x in range (0,2):
    for y in range (0,2):
        for z in range (0,2):
            for w in range (0,2):
                result = not(x <= y) or ((not w) <= (not z)) or w
                if (result == 0):
                    print (x, y, z, w)