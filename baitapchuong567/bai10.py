def don_so_sang_ben_trai():
    # Nhập chuỗi ký tự từ người dùng
    chuoi = input("Nhập vào chuỗi ký tự: ").strip()
    # Khởi tạo các biến để lưu các chữ số và ký tự
    chuoi_so = ""
    chuoi_ky_tu = ""
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu_hien_tai in chuoi:
        if ky_tu_hien_tai.isdigit():  # Nếu ký tự là chữ số
            chuoi_so += ky_tu_hien_tai
        else:  # Nếu ký tự không phải là chữ số, thêm vào phần ký tự
            chuoi_ky_tu += ky_tu_hien_tai
    # Kết hợp các chữ số và ký tự lại
    ket_qua = chuoi_so + chuoi_ky_tu
    # In kết quả
    print("Chuỗi mới sau khi dồn số sang bên trái: ", ket_qua)
# Gọi hàm
don_so_sang_ben_trai()
