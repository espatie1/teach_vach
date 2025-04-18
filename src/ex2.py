print('w x y z')
for w in [0, 1]:
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                F = z or (not((x <= y) <= (w and x)))
                print(w, x, y, z)
                break