giri = input('Lütfen Sevdiceğinizin İsimini Giriniz: ').lower()
print()
dict_1 = {"a": "Aklımı alıyor gözlerin o kadar olur",
          "b": "Ben nerde bir çift göz gördümse tuttum onu güzelce sana tamamladım",
          "c": "Cam bardağı tutuşuna bakılırsa, seni seviyorum",
          "ç": "Çocuklar ekmek yiyorlar gibidir sesin",
          "d": "Desem ki vakitlerden bir Nisan akşamıdır, rüzgarların en ferahlatıcısı senden esiyor",
          "e": "Ellerin o kadar beyaz ki artık o kadar olur",
          "f": "Fakat sen bir ümittin, bir misillemeydin yalnızlığa",
          "g": "Görüyorsun ya bir sevdayı büyütüyoruz seninle",
          "h": "Her sabah başlayan şeye doyamadık, düşümüz gerçeğimiz ne varsa yeryüzünde",
          "ı": "Israrla bir çiçek gibi tutarsın tuttuğun her şeyi",
          "i": "İkimiz birden sevinebiliriz, göğe bakalım",
          "j": "Jeneriğini koca bir denizin bir bardak suda görürdük",
          "k": "Kırmızı bir kuştur soluğum kumral göklerinde saçlarının",
          "l": "Lavantalar basar boynunun incesini Haziran'da, yalan mı",
          "m": "Mesela hatırla, denize hiç bakmadık çünkü kıyısındaydık",
          "n": "Ne güzel şey hatırlamak seni: bir mavi kumaşın üstünde unutulmuş elini ve saçlarını",
          "o": "Oysa ben senin gözlerinsiz edemem bilirsin",
          "ö": "Öyle düzeltici öyle yerine getiriciydi seni sevmek, ki Karaköy köprüsüne yağmur yağarken bıraksalar gökyüzü kendini ikiye bölecekti",
          "p": "Peygamber çiçeğinin aydınlığında ara sana doğru uzanan çaresiz ellerimi",
          "r": "Rahat mavi bir gökyüzü kuşanır baktığın uzak bozkır",
          "s": "Sesini yapan sözcüklerinden seviyorum seni",
          "ş": "Şu senin bulutsu sesin var ya uçtan uca tersyüz ediyor geceyi",
          "t": "Tutsam ellerinden ağlarsın, benek benek büyür karanlığım",
          "u": "Uzatmışsın ay aydınlık karanlığıma nereden uzatmışsan tenha boynunu",
          "ü": "Üzgün anlarında sesin kalınlaşıyor ya, keşke yalnız bunun için sevseydim seni",
          "v": "Ve sen sonunda bir gün çıkar gelirsin diye, çok şeyin adı küçük yazıldı",
          "y": "Yüzünün yarısı göz kadife yansımalı",
          "z": "Zaman kısa, otobüsler gidiyor, sen de beni sev"
          } 
          

for i in giri:
  if i in dict_1:
    sonuç = dict_1[i] 
    print(sonuç[0].upper() + sonuç[1:])
  if i == " ":
    print()