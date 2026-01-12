"""
Ushbu skript ('verify_ex03.py') 03-mashq (Exercise 03) natijalarini tekshirish uchun yozilgan.
Mashqning maqsadi: Ma'lumotlarni guruhlash (Grouping) va agregatsiya funksiyalaridan (median, count, nunique) foydalanishni o'rganish.

Vazifalar:
1.  Avvalgi mashqdan olingan `auto.json` faylini o'qish.
2.  `Make` (Marka) bo'yicha guruhlab, jarimalar (`Fines`) summasini emas, o'rtacha qiymatini (median) hisoblash.
3.  `Make` va `Model` bo'yicha guruhlab, jarimalar medianasini hisoblash.
4.  Qaysi avtomobil raqamida qancha jarima borligini hisoblash.
5.  Avtomobil raqamlari qancha turli xil modellar bilam bog'langanligini tekshirish.

Ishlatilgan kutubxonalar:
- `pandas`: Ma'lumotlarni o'qish, GroupBy mexanizmi va agregatsiya amallari (.median(), .count(), .nunique()) uchun.
"""

import pandas as pd

def verify():
    """
    Ex03 mashqini tekshiruvchi asosiy funksiya.
    'auto.json' faylini o'qib, ma'lumotlarni guruhlash (groupby) va agregatsiya qilish jarayonlarini tekshiradi.
    """
    try:
        # 1-qadam: Ma'lumotlarni yuklash.
        # '../ex02/auto.json' faylini o'qish.
        # orient='records' parametri JSON fayl tuzilishi qatorlar ro'yxatidan iborat ekanligini bildiradi.
        df = pd.read_json('../ex02/auto.json', orient='records')
        
        # 2-qadam: Indeksni o'rnatish.
        # 'CarNumber' (avtomobil raqami) ustunini indeks sifatida belgilash.
        # Bu qidiruvni tezlashtiradi va ma'lumotlar tuzilishini o'zgartiradi.
        df = df.set_index('CarNumber')
        
        # 3-qadam: Agregatsiyalarni tekshirish (Marka bo'yicha).
        # df.groupby('Make'): Jadvalni 'Make' ustuni qiymatlari bo'yicha guruhlarga ajratadi.
        # ['Fines']: Har bir guruhdan faqat 'Fines' ustunini oladi.
        # .median(): Har bir guruh uchun 'Fines' ning medianasini (o'rtadagi qiymatni) hisoblaydi.
        grouped = df.groupby('Make')['Fines'].median()
        print(f"SUCCESS: Median by Make calculated. Size: {len(grouped)}")
        
        # 4-qadam: Agregatsiyalarni tekshirish (Marka va Model bo'yicha).
        # Bu yerda guruhlash ikkita ustun bo'yicha amalga oshiriladi: avval Marka, keyin Model.
        grouped2 = df.groupby(['Make', 'Model'])['Fines'].median()
        print(f"SUCCESS: Median by Make/Model calculated. Size: {len(grouped2)}")
        
        # 5-qadam: Mashina raqami bo'yicha jarimalar soni.
        # groupby('CarNumber'): Mashina raqami bo'yicha guruhlash (garchi indeks bo'lsa ham groupby ishlata olamiz).
        # .count(): Har bir mashina raqami necha marta uchraganini hisoblaydi.
        # .sort_values(ascending=False): Natijani kamayish tartibida saralaydi (eng ko'p jarimasi borlar tepada).
        count = df.groupby('CarNumber')['Fines'].count().sort_values(ascending=False)
        # Natijani chiqarish: count.index[0] - eng ko'p jarimasi bor mashina raqami, count.iloc[0] - uning jarimalar soni.
        print(f"SUCCESS: Car number counts calculated. Top 1: {count.index[0]} with {count.iloc[0]} fines")
        
        # 6-qadam: Qo'shimcha tekshiruv (Mantiqiy test).
        # Bitta avtomobil raqamida bir nechta model bor-yo'qligini tekshirish.
        # .nunique(): Har bir guruhdagi 'Model' ustunida nechta unikal (takrorlanmas) qiymat borligini hisoblaydi.
        models_per_car = df.groupby('CarNumber')['Model'].nunique()
        
        # Filtrlash: Faqat 1 tadan ko'p modelga ega bo'lgan mashinalarni tanlash.
        multi_model = models_per_car[models_per_car > 1]
        print(f"INFO: Cars with multiple models: {len(multi_model)}")
        
    except Exception as e:
        print(f"FAILURE: Exception occurred: {e}")

if __name__ == "__main__":
    verify()
