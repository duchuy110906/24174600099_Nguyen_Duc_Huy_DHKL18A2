def tach_ho_ten():
    # Nhập họ tên từ người dùng
    ho_ten_day_du = input("Nhập vào họ tên đầy đủ: ").strip()
    # Tách họ tên thành danh sách các từ
    danh_sach_ten = ho_ten_day_du.split()
    # Lấy họ (từ đầu tiên) và tên (từ cuối cùng)
    ho = danh_sach_ten[0]
    ten = danh_sach_ten[-1]
    # Nếu có tên đệm, in tên đệm (bỏ qua trong kết quả)
    if len(danh_sach_ten) > 2:
        ten_dem = " ".join(danh_sach_ten[1:-1])
        print(f"Họ: {ho}, Tên đệm: {ten_dem}, Tên: {ten}")
    else:
        print(f"Họ: {ho}, Tên: {ten}")
# Gọi hàm
tach_ho_ten()
