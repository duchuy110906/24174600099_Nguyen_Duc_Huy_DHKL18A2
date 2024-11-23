#bai07
# Nhập vào một số n
n = int(input("Nhập vào một số n: "))

# Kiểm tra số nguyên tố
for num in range(2, n):  # Lặp qua các số từ 2 đến n-1
    is_prime = True  # Giả sử num là số nguyên tố
    for i in range(2, num):  # Kiểm tra xem num có chia hết cho i không
        if num % i == 0:
            is_prime = False  # Nếu chia hết, num không phải là số nguyên tố
            break
    if is_prime:
        print(num)  # In ra số nguyên tố