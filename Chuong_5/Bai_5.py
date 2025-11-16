def is_vowel(c):
    """Kiểm tra xem ký tự có phải là nguyên âm không."""
    return c.lower() in 'aeiou'

def is_consonant(c):
    """Kiểm tra xem ký tự có phải là phụ âm không."""
    return c.isalpha() and not is_vowel(c)

# Nhập chuỗi từ người dùng
s = input("Nhập chuỗi: ")

# Khởi tạo các biến đếm
count_upper = 0
count_lower = 0
count_digits = 0
count_special = 0
count_space = 0
count_vowels = 0
count_consonants = 0

# Duyệt qua từng ký tự trong chuỗi
for char in s:
    if char.isupper():  # Kiểm tra chữ IN HOA
        count_upper += 1
    elif char.islower():  # Kiểm tra chữ in thường
        count_lower += 1
    elif char.isdigit():  # Kiểm tra chữ số
        count_digits += 1
    elif char.isspace():  # Kiểm tra khoảng trắng
        count_space += 1
    elif char.isalpha():  # Kiểm tra chữ cái (loại bỏ ký tự đặc biệt)
        if is_vowel(char):  # Kiểm tra nguyên âm
            count_vowels += 1
        elif is_consonant(char):  # Kiểm tra phụ âm
            count_consonants += 1
    else:  # Các ký tự đặc biệt khác
        count_special += 1

# In kết quả
print(f"Số chữ IN HOA: {count_upper}")
print(f"Số chữ in thường: {count_lower}")
print(f"Số chữ là chữ số: {count_digits}")
print(f"Số ký tự đặc biệt: {count_special}")
print(f"Số khoảng trắng: {count_space}")
print(f"Số nguyên âm: {count_vowels}")
print(f"Số phụ âm: {count_consonants}")