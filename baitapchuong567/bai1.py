# Nhập chuỗi từ người dùng
chuoi = input("Nhập vào một chuỗi ký tự: ")
# Tách chuỗi thành các từ bằng phương thức split()
danh_sach_tu = chuoi.split()
# Tính số lượng từ trong danh sách
so_tu = len(danh_sach_tu)
# In ra số lượng từ
print("Số lượng từ trong chuỗi là:", so_tu)
