#bai 2
#nhap x
x = float(input("nhap gia tri cua x: "))
#kiem tra dieu kien cua x
if x > 0:
    #phep tinh
    tu_so = -x + (x**2 + 4)**(1/2)
    mau_so = (x**4 + 1)**(1/7)
    f_x = tu_so / mau_so
    #tinh
    ket_qua = round(f_x, 3)
    #in ket qua
    print("gia tri cua bieu thuc la:", ket_qua)
else:
    print("gia tri x phai lon hon 0 de thuc hien phep tinh.")
        