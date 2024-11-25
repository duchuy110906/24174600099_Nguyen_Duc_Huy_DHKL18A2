def kiem_tra_xau():
    # Nhập vào hai chuỗi str_1 và str_2
    str_1 = input("Nhập vào chuỗi str_1: ")
    str_2 = input("Nhập vào chuỗi str_2: ")
    # Kiểm tra xem str_2 có nằm trong str_1
    if str_2 in str_1:
        print(f"Chuỗi '{str_2}' có nằm trong '{str_1}' .")
    else:
        print(f"Chuỗi '{str_2}' không nằm trong '{str_1}' .")
    # Kiểm tra xem str_1 có nằm trong str_2
    if str_1 in str_2:
        print(f"Chuỗi '{str_1}' có nằm trong '{str_2}' .")
    else:
        print(f"Chuỗi '{str_1}' không nằm trong '{str_2}' .")
# Gọi hàm
kiem_tra_xau()
