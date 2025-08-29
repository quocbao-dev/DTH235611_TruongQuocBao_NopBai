# 🐍 Python Learning Notes

## 📌 Phần 1: Giới thiệu về Python
Python là một ngôn ngữ lập trình bậc cao, thông dịch, dễ học và dễ đọc.  
Nó được Guido van Rossum tạo ra và phát hành lần đầu vào năm 1991.  

🔹 **Đặc điểm nổi bật của Python:**
- Cú pháp đơn giản, dễ học.
- Thư viện phong phú cho nhiều lĩnh vực: AI, Machine Learning, Web, Data Science...
- Đa nền tảng (Windows, Linux, macOS).
- Hỗ trợ lập trình hướng đối tượng, thủ tục và hàm.

👉 Python rất phù hợp cho người mới bắt đầu cũng như các lập trình viên chuyên nghiệp.

---

## 📌 Phần 2: Các đoạn code cơ bản

### 1. Hello World
```python
print("Hello, World!")
#2. Biến và Kiểu dữ liệu

name = "Alice"       # Chuỗi (string)
age = 20             # Số nguyên (int)
height = 1.65        # Số thực (float)
is_student = True    # Boolean

print(name, age, height, is_student)

#3. Cấu trúc điều kiện (if-else)
python
Sao chép mã
x = 10
if x > 0:
    print("x là số dương")
else:
    print("x không phải số dương")
#4. Vòng lặp (for, while)

# Vòng lặp for
for i in range(5):
    print("Lần lặp thứ", i)

# Vòng lặp while
count = 0
while count < 3:
    print("Count =", count)
    count += 1
#5. Hàm (Function)

def greet(name):
    return "Xin chào " + name

print(greet("Alice"))

#6. Làm việc với danh sách (list)

numbers = [1, 2, 3, 4, 5]
numbers.append(6)        # Thêm phần tử
print(numbers[0])        # Truy cập phần tử đầu tiên
print(len(numbers))      # Độ dài danh sách

student = {"name": "Alice", "age": 20, "major": "IT"}
print(student["name"])
