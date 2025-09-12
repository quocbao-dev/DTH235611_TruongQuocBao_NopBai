a = 0
while a < 100:
    b = 0
    while b < 40:
        print(f"{a:02d}:{b:02d}")
        if (a + b) % 2 == 0:
            print('*', end=' ')
        b += 1
    print()
    a += 1