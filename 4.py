
# ?--- AŞAMA 4: ÖĞRETMEN ANLATIMI ---
# 'break' komutu, aradığımızı bulunca döngünün devam etmesini engeller.
# Bu örnek için rastgele sayılara ihtiyacımız var.
import random

print(" --- 'break' ile Döngüden Çıkma ---")
for i in range(1, 101):
    rastgele_sayi = random.randint(1, 100)
    print(f"Deneme #{i}: Üretilen sayı -> {rastgele_sayi}")
    if rastgele_sayi > 50:
        print("Hedef bulundu (50'den büyük bir sayı)! Döngüden çıkılıyor...")
        break # break komutu for döngüsünü burada kırar.
print("Döngü sona erdi.")

# !--- ÖĞRENCİ GÖREVİ ---
# Görev:
# 1. Kullanıcıdan `input()` ile 1-20 arasında bir "şanslı sayı" al.
# 2. Aldığın bu sayıyı `int()` ile tam sayıya çevir.
# 3. 1'den 20'ye kadar sayan bir `for` döngüsü kur.
# 4. Döngüdeki sayı, kullanıcının girdiği şanslı sayıya eşit olduğunda,
#    "Şanslı sayın bulundu!" yaz ve `break` ile döngüyü durdur.
# KODUNU BURAYA YAZMAYA BAŞLA:
