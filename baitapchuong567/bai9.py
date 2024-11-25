def kiem_tra_nhi_phan():
    # Nhập chuỗi nhị phân từ người dùng
    chuoi_nhi_phan = input("Nhập vào chuỗi ký tự nhị phân: ").strip()
    # Kiểm tra xem chuỗi chỉ chứa '0' và '1' và không trống
    if chuoi_nhi_phan and all(bit in '01' for bit in chuoi_nhi_phan):
        # Chuyển chuỗi nhị phân sang số thập phân
        so_thap_phan = int(chuoi_nhi_phan, 2)
        print(f"{chuoi_nhi_phan} là số nhị phân, chuyển sang thập phân: {so_thap_phan}")
    else:
        print("Chuỗi nhập vào không phải là số nhị phân hợp lệ")
# Gọi hàm
kiem_tra_nhi_phan()
