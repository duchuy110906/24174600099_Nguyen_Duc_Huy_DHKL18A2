def dem_ky_tu():
    # Nhập chuỗi từ người dùng
    chuoi_nhap = input("Nhập vào chuỗi ký tự: ")
    # Khởi tạo biến đếm
    so_chu = 0  # Đếm số ký tự là chữ
    so_so = 0  # Đếm số ký tự là số
    so_ky_tu_dac_biet = 0  # Đếm ký tự đặc biệt
    # Duyệt từng ký tự trong chuỗi
    for ky_tu in chuoi_nhap:
        if ky_tu.isalpha():  # Kiểm tra nếu là chữ cái
            so_chu += 1
        elif ky_tu.isdigit():  # Kiểm tra nếu là số
            so_so += 1
        else:  # Nếu không phải chữ cũng không phải số, là ký tự đặc biệt
            so_ky_tu_dac_biet += 1
    # In kết quả
    print(f"Số ký tự là chữ: {so_chu}")
    print(f"Số ký tự là số: {so_so}")
    print(f"Số ký tự đặc biệt: {so_ky_tu_dac_biet}")
# Gọi hàm
dem_ky_tu()
