#bai6
# Nhập vào một số từ người dùng
n = int(input("Nhập vào một số: "))

# Kiểm tra số chính phương
if n < 0:
    print(f"{n} không phải là số chính phương.")
else:
    # Tính căn bậc hai của n
    x = int(n ** 0.5)
    
    # Kiểm tra xem bình phương của x có bằng n không
    if x * x == n:
        print(f"{n} là số chính phương.")
    else:
        print(f"{n} không phải là số chính phương.")