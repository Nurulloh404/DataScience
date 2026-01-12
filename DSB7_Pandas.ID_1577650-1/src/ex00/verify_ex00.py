"""
Ushbu skript ('verify_ex00.py') 0-mashq (Exercise 00) natijalarini tekshirish uchun yozilgan.
Mashqning maqsadi: `feed-views.log` faylini tozalash, formatlash va `feed-views-semicolon.log` nomli yangi faylga saqlash.

Vazifalar:
1.  Asl log faylni (`../data/feed-views.log`) o'qish.
2.  Qatorlarni tozalash (skiprows, skipfooter).
3.  Ustunlarni nomlash.
4.  Indeksni sozlash.
5.  Natijani yangi faylga ';' (nuqta-vergul) ajratuvchisi bilan yozish.

Ishlatilgan kutubxonalar:
- `pandas`: Ma'lumotlarni o'qish, qayta ishlash va yozish uchun.
- `os`: Fayl tizimida fayllarning mavjudligini tekshirish uchun.
"""

import pandas as pd
import os

def verify():
    """
    Ex00 mashqini tekshiruvchi asosiy funksiya.
    Jarayon bosqichma-bosqich amalga oshiriladi va har bir bosqich terminalga chiqariladi.
    """
    try:
        # 1-qadam: Ma'lumotlarni o'qish.
        # pd.read_csv funksiyasi yordamida log fayl DataFrame ga yuklanadi.
        # Parametrlar sharhi:
        # - '../data/feed-views.log': O'qiladigan faylning nisbiy yo'li.
        # - skiprows=[2, 3]: Indeks raqami 2 va 3 bo'lgan qatorlarni (ya'ni 3 va 4-qatorlar) tashlab yuborish.
        #   Bu mashq shartida "noto'g'ri" ma'lumotlarni olib tashlash uchun talab qilingan bo'lishi mumkin.
        # - skipfooter=2: Faylning oxirgi 2 qatorini o'qimasdan tashlab yuborish.
        # - names=['datetime', 'user']: Faylda sarlavha (header) bo'lmagani uchun, ustunlarga qo'lda nom berish.
        # - engine='python': 'skipfooter' parametri ishlashi uchun 'python' motorini ishlatish kerak (C motori buni qo'llab-quvvatlamaydi).
        df = pd.read_csv('../data/feed-views.log', 
                        skiprows=[2, 3], 
                        skipfooter=2, 
                        names=['datetime', 'user'], 
                        engine='python')
        
        # 2-qadam: Indeksni o'zgartirish.
        # 'datetime' ustunini ushbu DataFrame ning indeksi (asosiy kaliti) sifatida belgilash.
        df = df.set_index('datetime')
        
        # 3-qadam: Indeks nomini o'zgartirish.
        # Indeksning nomini 'datetime' dan 'date_time' ga o'zgartiramiz.
        df.index.name = 'date_time'
        
        # Natijaviy fayl nomi
        output_file = 'feed-views-semicolon.log'
        
        # 4-qadam: Natijani saqlash.
        # DataFrame ni CSV formatida saqlash.
        # sep=';': Ustunlarni vergul (,) o'rniga nuqta-vergul (;) bilan ajratish.
        df.to_csv(output_file, sep=';')
        
        # 5-qadam: Tekshirish (Verifikatsiya).
        # os.path.exists() yordamida fayl yaratilganligini tekshiramiz.
        if os.path.exists(output_file):
            print(f"SUCCESS: {output_file} created.")
            
            # Fayl tarkibini qo'shimcha tekshirish
            with open(output_file, 'r') as f:
                # Birinchi qatorni (sarlavhani) o'qib olish
                header = f.readline().strip()
                # Sarlavha kutilgan formatda ekanligini tekshirish ("date_time;user")
                if header == "date_time;user":
                    print("SUCCESS: Header is correct.")
                else:
                    print(f"FAILURE: Header is incorrect: {header}")
        else:
            print(f"FAILURE: {output_file} not created.")
            
    except Exception as e:
        # Xatolik yuz bersa, uni ushlab qolish va terminalga chiqarish
        print(f"FAILURE: Exception occurred: {e}")

if __name__ == "__main__":
    verify()
