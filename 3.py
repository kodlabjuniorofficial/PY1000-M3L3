
# ? --- AŞAMA 3: ÖĞRETMEN ANLATIMI ('and' kullanımı) ---
print("\\n--- 'and' ile Çoklu Şart ---")
# 1'den 50'ye kadar sayalım ve HEM 3'e HEM DE 5'e tam bölünen sayıları bulalım.
for i in range(1, 51):
    # `and` kelimesi, her iki şartın da DOĞRU olması gerektiğini söyler.
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} sayısı hem 3'e hem de 5'e tam bölünüyor!")

# ! --- ÖĞRENCİ GÖREVİ ('or' kullanımı) ---
# Görev: 1'den 30'a kadar sayan bir döngü kur.
# Eğer sayı 10'dan küçükse VEYA 25'ten büyükse ekrana yazdır. (`or` kullan)
# KODUNU BURAYA YAZMAYA BAŞLA: