import math
#nhap gia tri x
x = float(input("nhap gia tri x: "))
#kiem tra dieun kien cua x
if x > 0:
    #phep tinh
    log_4_x = math.log(x, 4)
    log_x_2 = math.log(2, x)
    #tinh
    dap_an = log_4_x + log_x_2 
    dap_an = round(dap_an, 2)
    #ket qua
    print("gia tri cua bieu thuc la", dap_an)
else:
    print("gia tri x phai lon hon 0 de thuc hien phep tinh")
        