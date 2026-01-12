"""
Ushbu skript ('verify_ex01.py') 01-mashq (Exercise 01) natijalarini tekshirish uchun yozilgan.
Mashqning maqsadi: Vaqtlar (timestamp) bilan ishlash, jumladan sanani qismlarga ajratish va kunning qaysi vaqti (daytime) ekanligini aniqlash.

Vazifalar:
1.  Log faylni o'qish.
2.  `datetime` ustunini haqiqiy sana formatiga (datetime object) o'tkazish.
3.  Sanadan yil, oy, kun, soat, daqiqa, soniyalarni ajratib olish va alohida ustunlarga yozish.
4.  `daytime` (kun qismi) ustunini yaratish: soatga qarab 'morning', 'afternoon' va hokazolarga bo'lish.
5.  Foydalanuvchilarni asosiy indeks qilib belgilash.
6.  Turli statistikalar (count, mode) hisoblash.

Ishlatilgan kutubxonalar:
- `pandas`: Ma'lumotlarni qayta ishlash, vaqt bilan ishlash (dt accessor) va guruhlash (cut) uchun.
- `numpy`: Asosan pandas bilan birga keladigan ma'lumot turlari uchun.
"""

import pandas as pd
import numpy as np

def verify():
    """
    Ex01 mashqini tekshiruvchi asosiy funksiya.
    Bu funksiya 'feed-views.log' faylini o'qib, sana va vaqt bilan ishlashni tekshiradi,
    jumladan vaqt bo'laklarini ajratish va kun qismlariga (daytime) bo'lish.
    """
    try:
        # 1-qadam: Ma'lumotlarni yuklash.
        # '../data/feed-views.log' faylini o'qiymiz.
        # names=['datetime', 'user'] - Faylda sarlavha yo'qligi uchun ustun nomlarini o'zimiz beramiz.
        # engine='python' - ba'zi murakkab o'qish operatsiyalari uchun kerak (bu yerda majburiy emas, lekin ishonchli).
        views = pd.read_csv('../data/feed-views.log', 
                            names=['datetime', 'user'], 
                            engine='python')
        
        # 2-qadam: Datetime konvertatsiyasi.
        # 'datetime' ustuni hozircha shunchaki matn (string) ko'rinishida.
        # Uni pandas tushunadigan 'datetime64' formatiga o'tkazamiz.
        views['datetime'] = pd.to_datetime(views['datetime'])
        
        # 3-qadam: Vaqt birliklarini ajratish.
        # .dt (datetime accessor) orqali sananing ichki qismlariga murojaat qilamiz.
        views['year'] = views['datetime'].dt.year       # Yil
        views['month'] = views['datetime'].dt.month     # Oy
        views['day'] = views['datetime'].dt.day         # Kun
        views['hour'] = views['datetime'].dt.hour       # Soat (0-23)
        views['minute'] = views['datetime'].dt.minute   # Daqiqa
        views['second'] = views['datetime'].dt.second   # Soniya
        
        # 4-qadam: Kun qismlariga ajratish (Binning).
        # Kunni quyidagi qismlarga bo'lamiz:
        # - night (tun): 00:00 - 03:59
        # - early morning (erta tong): 04:00 - 06:59
        # - morning (tong): 07:00 - 10:59
        # - afternoon (tushlikdan keyin): 11:00 - 16:59
        # - early evening (erta oqshom): 17:00 - 19:59
        # - evening (oqshom): 20:00 - 23:59
        labels = ['night', 'early morning', 'morning', 'afternoon', 'early evening', 'evening']
        
        # Chegaralar (bins).
        # [-1, 3] -> 0, 1, 2, 3 soatlar (night)
        # (3, 6] -> 4, 5, 6 soatlar (early morning) va h.k.
        bins = [-1, 3, 6, 10, 16, 19, 23]
        
        # pd.cut funksiyasi sonli qiymatlarni (soatni) intervallarga (bins) bo'lib, tegishli nom (label) beradi.
        views['daytime'] = pd.cut(views['hour'], bins=bins, labels=labels)
        
        # 5-qadam: Indeksni sozlash.
        # 'user' ustunini indeks (index) sifatida belgilaymiz.
        views = views.set_index('user')
        
        # 6-qadam: Tekshirish va statistika.
        # Jami qatorlar sonini hisoblash.
        count = views.count()
        print(f"SUCCESS: Count calculated: {count['datetime']}")
        
        # Har bir kun qismi (morning, night va h.k.) qancha marta uchraganini hisoblash.
        daytime_counts = views['daytime'].value_counts()
        print(f"SUCCESS: Daytime counts calculated: {daytime_counts.sum()}")
        
        # Ma'lumotlar soni 500 ta ekanligini tekshirish (chunki biz 500 ta generatsiya qilgandik).
        if count['datetime'] == 500: 
             print("SUCCESS: Count matches generated data.")
        
        # Saralashni tekshirish (o'sish tartibida: soat -> daqiqa -> soniya).
        views_sorted = views.sort_values(by=['hour', 'minute', 'second'])
        
        # Modani (eng ko'p uchraydigan soat) hisoblash.
        # .mode() eng ko'p uchraydigan qiymatlarni Series sifatida qaytaradi (chunki moda bir nechta bo'lishi mumkin).
        # [0] orqali birinchisini olamiz.
        mode_hour = views['hour'].mode()[0]
        print(f"SUCCESS: Mode hour: {mode_hour}")
        
    except Exception as e:
        print(f"FAILURE: Exception occurred: {e}")

if __name__ == "__main__":
    verify()
