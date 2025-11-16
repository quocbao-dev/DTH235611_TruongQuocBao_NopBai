import re
print ("Nhập một chuỗi: ")
s= input ()
Soam = re.findall(r'-\d+', s)
print (Soam)