raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

while True :
    choice = int(input('''
===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====
1. Hiển thị chuỗi mã vạch gốc
2. Giải mã, làm sạch và in báo cáo kiểm kê
3. Tra cứu nhanh theo đuôi Serial
4. Thoát chương trình
Nhập lựa chọn của bạn (1-4): '''))
    
    if choice == 4 :
        print('Chương trình đã dừng !')
        break

    elif choice == 1 :
        print('Chuỗi mã vạch gốc : ' , raw_batch)
    