def kiem_tra_so_thap_phan():
    # Nhập chuỗi từ người dùng
    chuoi = input("Nhập vào chuỗi ký tự: ").strip()
    # Kiểm tra nếu chuỗi là số thập phân hợp lệ
    if chuoi.count('.') == 1 and chuoi.replace('.', '').isdigit() and chuoi != ".":
        print("Đây là một số thập phân")
    else:
        print("Đây không phải là số thập phân")
# Gọi hàm
kiem_tra_so_thap_phan()
