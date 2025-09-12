day = int(input('Nhập vào một ngày: '))
month = int(input('Nhập vào một tháng: '))
year = int(input('Nhập vào một năm: '))

if month < 1 or month > 12:
    print('Tháng không hợp lệ')
elif day < 1 or day > 31:
    print('Ngày không hợp lệ')
elif year < 0:
    print('Năm không hợp lệ')
elif month in [4, 6, 9, 11] and day > 30:
    print('Ngày không hợp lệ')
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if day > 29:
            print('Ngày không hợp lệ')
        else:
            print('Ngày hợp lệ')
    else:
        if day > 28:
            print('Ngày không hợp lệ')
        else:
            print('Ngày hợp lệ')
