#bai15
# Chuyển từ cơ số 10 sang cơ số 2
n = int(input("Nhập số thập phân: "))
if n == 0:
    print("Số nhị phân là: 0")
else:
    # In trực tiếp các bit nhị phân từ phải sang trái
    while n > 0:
        print(n % 2, end= "")
        n //= 2
    print()  # Xuống dòng sau khi in xong

# Chuyển từ cơ số 2 sang cơ số 10
b = input("Nhập số nhị phân: ")
thap_phan = 0
for i in range(len(b)):
    thap_phan = thap_phan * 2 + int(b[i])
print(f"Số thập phân là: {thap_phan}")