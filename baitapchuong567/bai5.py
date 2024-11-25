def dem_hoa_va_chu_thuong():
    # Nhập chuỗi từ người dùng
    chuoi_nhap = input("Nhập vào chuỗi ký tự: ")
    # Khởi tạo biến đếm
    so_chu_hoa = 0  # Đếm số chữ cái viết hoa
    so_chu_thuong = 0  # Đếm số chữ cái viết thường
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi_nhap:
        if ky_tu.isupper():  # Kiểm tra nếu là chữ cái viết hoa
            so_chu_hoa += 1
        elif ky_tu.islower():  # Kiểm tra nếu là chữ cái viết thường
            so_chu_thuong += 1
    # In kết quả
    print(f"Số chữ cái viết hoa: {so_chu_hoa}")
    print(f"Số chữ cái viết thường: {so_chu_thuong}")
    # Gọi hàm
dem_hoa_va_chu_thuong()
