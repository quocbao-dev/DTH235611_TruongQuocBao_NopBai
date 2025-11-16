import math
def CanBac2LongNhau(n):
    if n == 1:
        return math.sqrt(2)
    else:
        return math.sqrt(2 + CanBac2LongNhau(n - 1))

print('Chương trình tính căn bậc lồng nhau: ')
n = int(input('Nhập n: '))
result = CanBac2LongNhau(n)
print(f'S = ',result)