def weight_conversion():
    berat = int(input("Masukan Angka > "))
    satuan = input("Dalam satuan apa berat yang anda masukan? (K untuk KG, L untuk LBS) > ")

    if satuan.lower() == 'l':
        print(f"Berat anda dikonversi menjadi kilogram adalah {round(berat * 0.453592)} kg")
    elif satuan.lower() == 'k':
        print(f"Berat anda dikonversi menjadi pons adalah {round(berat * 2.20462)} lbs")
weight_conversion()