from math import sqrt

print('Chương trình tính độ dài đoạn AB: ')
Xa = int(input('Nhập tọa độ Xa: '))
Xb = int(input('Nhập tọa độ Xb: '))
Ya = int(input('Nhập tọa độ Ya: '))
Yb = int(input('Nhập tọa độ Yb: '))


AB = sqrt((Xb - Xa)**(Xb - Xa) + (Yb - Ya)**(Yb - Ya))
result = abs(AB)
print('Chiều dài đoạn AB là: ',result)