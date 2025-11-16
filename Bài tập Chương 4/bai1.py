from math import sqrt

print('Chương trình tính diện tích Tam Giác')
a=float(input('Nhập số a>0: '))
b=float(input('Nhâp số b>0: '))
c=float(input('Nhập số c>0: '))
if (a<=0 or b<=0 or c<=0) or a+b<=c or b+c<=a or c+a<=b:
    print('Tam giác không hợp lệ!!!')
else:
    cv = a+b+c
    p=cv/2
    dt=sqrt(p*(p-a)*(p-b)*(p-c))
    print('Diện tích tam giác = ', dt)