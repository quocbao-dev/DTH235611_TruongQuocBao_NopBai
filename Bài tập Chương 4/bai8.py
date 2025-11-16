import math

print('Chương trình tính hàm Logarit: ')
x = int(input('Nhập số x > 0: '))
a = int(input('Nhâp số a > 0: '))
log_a_x = math.log(x,a)
print('Logarit có số {0} của {1} là: {2}'.format(a,x,log_a_x))
print("Logit co so "+a+" cua "+x+" la "+log_a_x)