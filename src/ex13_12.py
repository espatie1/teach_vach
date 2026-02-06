oct1=191
oct2=239
oct3=130
oct4=3

mask1=255
mask2=255
# mask3=A
mask4=0

ads1=oct1&mask1
ads2=oct2&mask2
# ads3=oct3&mask3
ads4=oct4&mask4

def octet_count_1(x):
    return bin(x).count("1")

count=0

# Маска сети может быть только с подряд идущими единицами слева направо (либо без единиц вообще)
# То бишь возможны лишь
# 0000 0000 = 0
# 1000 0000 = 128
# 1100 0000 = 192
# 1110 0000 = 224
# 1111 0000 = 240
# 1111 1000 = 248
# 1111 1100 = 252
# 1111 1110 = 254
# 1111 1111 = 255
for A in {0,128,192,224,240,248,252,254,255}:
    mask3=A
    ads3=oct3&mask3
    vse_adresa = True
    for octet3 in range(ads3, ads3 + (255 - mask3) + 1):
        for octet4 in range(256):
            left=octet_count_1(ads1)+octet_count_1(ads2)
            right=octet_count_1(octet3)+octet_count_1(octet4)
            if left < right:
                vse_adresa = False
                break
        if not vse_adresa:
            break
    if vse_adresa:
        print(A)
        break
        
            