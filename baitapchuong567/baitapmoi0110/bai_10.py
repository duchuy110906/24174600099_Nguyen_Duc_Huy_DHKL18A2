#bai10
# Nhập hai số từ người dùng
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Áp dụng thuật toán Euclid để tìm UCLN
while b != 0:
    a, b = b, a % b

# In ra kết quả
print(f"Ước chung lớn nhất của hai số là: {a}")