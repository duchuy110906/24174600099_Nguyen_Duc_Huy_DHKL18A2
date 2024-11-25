def kiem_tr_so_am():
    # Nhập chuỗi từ người dùng
    chuoi = input("Nhập vào chuỗi ký tự: ").strip()
    # Kiểm tra nếu chuỗi bắt đầu bằng dấu '-' và phần còn lại là số
    if chuoi.startswith('-') and chuoi[1:].isdigit():
        print("Đây là một số âm")
    else:
        print("Đây không phải là số âm")
        # Gọi hàm
kiem_tr_so_am()
