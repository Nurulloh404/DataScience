def data_types():
    # 'int' (Integer) - Butun sonlar turi.
    # Sintaksis: O'zgaruvchi nomi = qiymat.
    int_var = 10
    
    # 'str' (String) - Matnli ma'lumotlar. Qo'shtirnoq ("") yoki birtirnoq ('') ichida yoziladi.
    str_var = "Hello"
    
    # 'float' - O'nlik kasr sonlar (suzuvchi nuqtali sonlar).
    # Nuqta (.) butun va kasr qismini ajratish uchun ishlatiladi.
    float_var = 10.0
    
    # 'bool' (Boolean) - Mantiqiy qiymat. Faqat 'True' (rost) yoki 'False' (yolg'on) bo'lishi mumkin.
    # Python'da True/False katta harf bilan boshlanishi shart.
    bool_var = True
    
    # 'list' (Ro'yxat) - Bir nechta elementlarni saqlash uchun ishlatiladi.
    # Sintaksis: Kvadrat qavs [] ichida, elementlar vergul bilan ajratiladi.
    # Ro'yxatlar o'zgaruvchan (mutable) - ya'ni ularni yaratgandan keyin o'zgartirsa bo'ladi.
    list_var = [1, 2, 3]
    
    # 'dict' (Dictionary/Lug'at) - Kalit-qiymat (Key-Value) juftligini saqlaydi.
    # Sintaksis: Jingalak qavs {} ichida "kalit: qiymat" ko'rinishida yoziladi.
    # Masalan, "a" kaliti orqali 1 qiymatini olish mumkin.
    dict_var = {"a": 1, "b": 2}
    
    # 'tuple' (Kortej) - Ro'yxatga o'xshaydi, lekin o'zgarmas (immutable).
    # Sintaksis: Oddiy qavs () ichida yoziladi. Yaratilgandan keyin elementlarini o'zgartirib bo'lmaydi.
    tuple_var = (1, 2, 3)
    
    # 'set' (To'plam) - Takrorlanmas elementlardan iborat tartibsiz to'plam.
    # Sintaksis: Jingalak qavs {} ichida yoziladi (lekin kalit:qiymatsiz).
    # Bu yerda har bir raqam noyob bo'lishi kafolatlanadi.
    set_var = {1, 2, 3}
    
    # List comprehension (Ro'yxat generatori) sintaksisi ishlatilmoqda.
    # type(o'zgaruvchi) - bu funksiya o'zgaruvchining turini (class) qaytaradi.
    # .__name__ - bu atribut ushbu tur (class) ning nomini satr ko'rinishida beradi (masalan 'int').
    all_types = [
        type(int_var).__name__, 
        type(str_var).__name__, 
        type(float_var).__name__, 
        type(bool_var).__name__, 
        type(list_var).__name__, 
        type(dict_var).__name__, 
        type(tuple_var).__name__, 
        type(set_var).__name__
    ]
    
    # f-string (Formatlangan satr) sintaksisi: f"..."
    # Bu satr ichida {} qavslar orasida Python kodini yoki o'zgaruvchilarni to'g'ridan-to'g'ri yozish imkonini beradi.
    # ', '.join(all_types) - Satrlar metodlari.
    # .join() metodi ro'yxatdagi (all_types) barcha so'zlarni ', ' (vergul va probel) bilan birlashtirib,
    # bitta uzun satr hosil qiladi.
    print(f"[{', '.join(all_types)}]")
  
# Ushbu shart fayl to'g'ridan-to'g'ri ishga tushirilganda nima bo'lishini belgilaydi.
# __name__ o'zgaruvchisi Python tomonidan avtomatik yaratiladi.
# Agar fayl asosiy dastur sifatida ishga tushsa, uning qiymati '__main__' bo'ladi.
# Agar modul sifatida import qilinsa, fayl nomi bo'ladi.
if __name__ == '__main__':
    # data_types() funksiyasini chaqirish (run qilish).
    data_types()
