def ToiUuChuoi (s):
    s2= s
    s2 = s2.strip()
    arr= s2.split (' ')
    s2 =' '
    for x in arr:
        word =x
        if len(word.strip())!=0:
            s2= s2+word +' '
    return s2.strip ()
print ("Nhập một chuỗi:")
s= input ()
s= ToiUuChuoi(s)
s.lower()
s.capitalize()
print(s)


#chuoi.lower(): Chuyển tất cả các ký tự trong chuỗi thành chữ thường.
#chuoi.capitalize(): Viết hoa chữ cái đầu tiên của chuỗi.
