
for x in range(2735, 0, -1):
    test = 5**2025 + 5**1500 - x
    nuli = 0
    while (test > 1):
        if (test % 5 == 0):
            nuli = nuli + 1
        test = test // 5
    if(nuli == 527):
        print(x)
        break