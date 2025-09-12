import math
def tinh_s(x, n):
    s = 0
    for i in range(n + 1):
        s = s + (x ** (2*i+1)) / math.factorial(2*i+1)
    return s

x =float(input("Nhập x: "))
n = int(input("Nhập n: "))
print('Nhập giá trị S(x,n) =', tinh_s(x, n))