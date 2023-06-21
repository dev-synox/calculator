print("""---------------------------------------
Hoş Geldiniz...

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi

5. Karekök Alma İşlemi
---------------------------------------""")
işlem = input("iŞLEM NUMARASINI GİRİNİZ:")

a = int(input("Birinci Sayı:"))
b = int(input("ikinci Sayı:"))


if (işlem == "1"):
    print("{} ile {} 'nin toplamı: {}".format(a,b,a+b))
elif (işlem == "2"):
    print("{} ile {} 'nin farkı: {}".format(a,b,a-b))
elif (işlem == "3"):
    print("{} ile {} 'nin çarpımı: {}".format(a,b,a*b))
elif (işlem == "4"):
    print("{} ile {} 'nin bölümü: {}".format(a,b,a/b))
elif (işlem == "5"):
    print("{} ile {} 'nin karekökü: {}".format(a,b,a*a*b))

else:
    print("lütfen geçerli işlem yapınız.")
    quit()