a = float(input('Nhập số a: '))
b = float(input('Nhập số b: '))
op = input('Nhập phép toán (+, -, *, /): ')

if op == '+' :
    print(f'Kết quả phép toán: {a + b} ')
elif op == '-' :
    print(f'Kết quả phép toán: {a - b} ')
elif op == '*' :
    print(f'Kết quả phép toán: {a * b} ')
elif op == '/' :
    if b != 0 :
        print(f'Kết quả phép toán: {a / b} ')
    else :
        print('Lỗi: Không thể chia cho 0!')
else :
    print('Lỗi: Phép toán không hợp lệ!')