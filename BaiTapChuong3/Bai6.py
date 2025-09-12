def doc_so(n):
    donvi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 10:
        return donvi[n]
    elif 10 <= n <= 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + donvi[n % 10]

    else:
        hang_chuc = n // 10
        hang_dv = n % 10
        if hang_dv == 0:
            return chuc[hang_chuc]
        elif hang_dv == 5:
            return chuc[hang_chuc] + " lăm"
        else:
            return chuc[hang_chuc] + " " + donvi[hang_dv]


n = int(input("Nhập số n (0 < n < 100): "))
print('Cách đọc số:', doc_so(n))