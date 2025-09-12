x = int(input('Nhâp số x: '))
n = int(input('Nhập số n: '))
s=0
for i in range(1, n + 1):
    tu = x**i
    mau = 1
    for j in range(1, i + 1):
        mau =mau * j
    s = s + (tu/mau)
print(f"S({x},{n})={s}")