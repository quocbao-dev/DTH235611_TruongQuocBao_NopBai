def hinh1(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def hinh2(n):
    for i in range(1,n+1):
        print('*'*i)

def hinh3(n):
    for i in range(1,n+1):
        if i <= n // 2:
            print('* '*i)
        else:
            print('* '*(n-i+1))

#Chương trình chính
n = int(input('Nhập n: '))
print('Chọn hình muốn vẽ: ')
chon = int(print('Nhập số (1 -> 3): '))
if chon == 1:
    hinh1(n)
elif chon == 2:
    hinh2(n)
elif chon == 3:
    hinh3(n)
else:
    print('Chọn sai, mời chọn lại!')