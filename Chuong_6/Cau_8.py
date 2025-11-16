from random import randrange

n = int(input("Nhap số phần tử mảng: "))
lst = [0]*n

for i in range(n):
  lst[i] = randrange(-100, 100)

print("Mảng ngẫu nhiên: ")
print(lst)

for i in range(n - 1):
  for j in range(i + 1, n):
    if lst[i] > lst[j]:
      lst[i], lst[j] = lst[j], lst[i]

print("Mảng sau khi sắp xếp: ")
print(lst)