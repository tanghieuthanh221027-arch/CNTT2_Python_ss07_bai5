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
        print('Đóng ca kiểm kho. Chào tạo biệt!')
        break

    elif choice == 1 :
        print('Chuỗi mã vạch gốc : ' , raw_batch)
    
    elif choice == 2:
        products = raw_batch.split(';')
        valid_products = 0
        total_products = len(products)

        print(f'''
{"MÃ SP":<10} | {"XUẤT XỨ":<10} | {"NĂM SX":<10} | {"SERIAL":<10} | {"TRẠNG THÁI"}
{"-" * 70}
''')

        for product in products :
            clean_product = product.strip().upper()
            product_type , country , year , serial = clean_product.split('-')
            full_year = '20' + year

            if serial.isdigit() :
                status = 'Pass'
                valid_products += 1
            else :
                status = 'Lỗi Serial - Reject'

            print(f'''
{product_type:<10} | {country:<10} | {full_year:<10} | {serial:<10} | {status}
''')

        print(f'''
Đã giải mã thành công {valid_products} sản phẩm hợp lệ / Tổng số {total_products} sản phẩm.
''')

    elif choice == 3 :
        search_serial = input('Nhập 2 số cuối của Serial cần tìm : ').strip()
        found = False
        products = raw_batch.split(';')

        for product in products :
            clean_product = product.strip().upper()
            product_type , country , year , serial = clean_product.split('-')

            if serial[-2:] == search_serial :
                full_year = '20' + year
                print(f'''
Mã SP : {product_type}
Xuất xứ : {country}
Năm SX : {full_year}
Serial : {serial}
''')
                found = True

        if found == False :
            print('Không tìm thấy sản phẩm phù hợp!')
    else :
        print('Chức năng không tồn tại, vui lòng nhập số từ 1-4!')
