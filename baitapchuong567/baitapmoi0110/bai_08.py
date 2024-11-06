#bai08
# Nhập vào số n
n = int(input("Nhập vào n: "))

# Duyệt qua tất cả các số từ 2 đến n-1 để kiểm tra số hoàn hảo
print(f"Các số hoàn hảo nhỏ hơn {n}:")
for i in range(2, n):
    total = 1  # Bắt đầu tổng từ 1 vì 1 là ước của tất cả các số
    # Tính tổng các ước của i
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            total += j
            if j != i // j:  # Tránh tính lại ước đôi
                total += i // j
    # Kiểm tra nếu tổng các ước bằng chính số đó
    if total == i:
        print(i)
