def so_ngay_trong_thang(thang, nam):
    if thang == 2:
        return 29 if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0) else 28
    return 31 if thang in {1, 3, 5, 7, 8, 10, 12} else 30

def main():
    thang = int(input("Nhập số tháng (từ 1 đến 12): "))
    nam = int(input("Nhập năm: "))

    so_ngay = so_ngay_trong_thang(thang, nam)
    print(f"Số ngày trong tháng {thang} năm {nam} là : {so_ngay}")

if __name__ == "__main__":
    main()
 
