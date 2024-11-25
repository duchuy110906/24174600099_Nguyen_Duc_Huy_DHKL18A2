def loai_bo_khoang_trang_thua():
    # Nhập chuỗi từ người dùng
    chuoi_nhap = input("Nhập vào chuỗi ký tự: ").strip()
    # Khởi tạo chuỗi kết quả
    ket_qua = ""
    n = len(chuoi_nhap)
    # Duyệt qua từng ký tự bằng chỉ số
    for i in range(n):
        # Thêm ký tự nếu không phải là khoảng trắng hoặc nếu là khoảng trắng nhưng không đứng liền trước khoảng trắng khác
        if chuoi_nhap[i] != ' ' or (i > 0 and chuoi_nhap[i - 1] != ' '):
            ket_qua += chuoi_nhap[i]
    # In chuỗi kết quả
    print(f"Chuỗi sau khi loại bỏ dấu cách thừa: {ket_qua}")
# Gọi hàm
loai_bo_khoang_trang_thua()
