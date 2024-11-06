#bai11
# Nhập vào hai số từ người dùng
a = int(input("Nhập vào số thứ nhất: "))
b = int(input("Nhập vào số thứ hai: "))

# Tính GCD (Ước chung lớn nhất) bằng thuật toán Euclid
x, y = a, b
while y != 0:
    x, y = y, x % y

# In ra BCNN trực tiếp mà không cần biến phụ
print(f"Bội chung nhỏ nhất của {a} và {b} là: {abs(a * b) // x}")