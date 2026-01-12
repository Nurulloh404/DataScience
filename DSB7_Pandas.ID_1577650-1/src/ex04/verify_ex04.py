"""
Ushbu skript ('verify_ex04.py') 04-mashq (Exercise 04) natijalarini tekshirish uchun yozilgan.
Mashqning maqsadi: Ma'lumotlarni birlashtirish (concatenation), yangi ustunlar qo'shish (Year) va ma'lumotlarni boyitish (surname.json dan familiyalarni qo'shish).

Vazifalar:
1.  `auto.json` faylini o'qish.
2.  Mavjud ma'lumotlarga tasodifiy tanlangan qo'shimcha 200 ta qatorni qo'shish (sample).
3.  `Year` (Ishlab chiqarilgan yili) ustunini yaratish va 1980-2019 yillar oralig'idagi tasodifiy qiymatlar bilan to'ldirish.
4.  Barcha avtomobil egalari uchun familiyalar (`SURNAME`) generatsiya qilish:
    - Familiyalar `surname.json` faylidan olinadi.
    - Har bir unikal avtomobil raqami uchun bitta familiya biriktiriladi.
5.  Natijalarni ikki xil faylga saqlash:
    - `fines.csv`: Avtomobillar haqida to'liq ma'lumot (jarimalar, yil va h.k.).
    - `owners.csv`: Avtomobil raqami va egasining familiyasi.

Ishlatilgan kutubxonalar:
- `pandas`: Jadvallarni o'qish (read_json), birlashtirish (concat), namuna olish (sample) va yozish (to_csv) uchun.
- `numpy`: Tasodifiy sonlar (yil) va tanlovlar (familiya) uchun.
- `json`: Familiyalar ro'yxatini JSON fayldan o'qish uchun.
- `os`: Fayl tizimi bilan ishlash uchun.
"""

import pandas as pd
import numpy as np
import json
import os

def verify():
    """
    Ex04 mashqini tekshiruvchi asosiy funksiya.
    'auto.json' faylini o'qib, ma'lumotlarni kengaytiradi va yangi jadvallar hosil qiladi.
    """
    try:
        # 1-qadam: Asosiy faylni o'qish.
        # '../ex02/auto.json' faylini o'qish.
        df = pd.read_json('../ex02/auto.json', orient='records')
        
        # 2-qadam: Namuna olish (Sampling).
        # Asosiy jadvaldan 200 ta tasodifiy qatorni tanlab olamiz.
        # random_state=21: Natija har doim bir xil bo'lishini ta'minlash uchun (takrorlanuvchanlik).
        sample = df.sample(200, random_state=21)
        
        # 3-qadam: Birlashtirish (Concatenation).
        # Asosiy jadval (df) va tanlab olingan namuna (sample) ni birlashtiramiz.
        # Natijada qatorlar soni oshadi.
        concat_rows = pd.concat([df, sample])
        
        # Tekshirish: Qatorlar soni kutilganidek oshdimi?
        if concat_rows.shape[0] == df.shape[0] + 200:
             print(f"SUCCESS: Sample concatenated correctly. Size: {concat_rows.shape[0]}")
        
        # 4-qadam: Yil ustunini qo'shish.
        # np.random.seed(21): Tasodifiy sonlar generatorini sozlash.
        np.random.seed(21)
        
        # 1980 dan 2020 gacha (2020 kirmaydi) bo'lgan oraliqda tasodifiy yillarni generatsiya qilish.
        # size=len(concat_rows): Nechta qator bo'lsa, shuncha yil yaratiladi.
        years = np.random.randint(1980, 2020, size=len(concat_rows))
        
        # Yangi 'Year' ustunini yaratish va qiymatlarni yozish.
        concat_rows['Year'] = years
        
        # O'zgaruvchini 'fines' deb nomlash (mashq shartiga ko'ra).
        fines = concat_rows
        
        # 5-qadam: Familiyalarni yuklash.
        # '../../datasets/surname.json' faylidan familiyalar ro'yxatini o'qish.
        with open('../../datasets/surname.json') as f:
            surnames_json = json.load(f)
        
        # JSON fayl odatda ro'yxatlar ro'yxati (list of lists) yoki murakkabroq tuzilishga ega bo'lishi mumkin.
        # Agar familiyalar ro'yxatning birinchi elementida joylashgan bo'lsa (masalan [['Ivanov', ...], ...]), ularni ajratib olamiz.
        # [1:] - sarlavhani tashlab yuborish uchun (agar birinchi qator sarlavha bo'lsa).
        surnames = [row[0] for row in surnames_json[1:]]
            
        # 6-qadam: Avtomobil egalarini aniqlash.
        # 'CarNumber' ustunidagi unikal (takrorlanmas) qiymatlarni ajratib olish.
        unique_cars = fines['CarNumber'].unique()
        
        np.random.seed(21)
        # Har bir unikal mashina raqami uchun familiyalar ro'yxatidan tasodifiy bittasini tanlash.
        if isinstance(surnames, list):
             sampled_surnames = np.random.choice(surnames, size=len(unique_cars))
        else:
             # Ehtiyot chorasi: agar familiyalar ro'yxati kutilganidek bo'lmasa, sun'iy familiyalar yaratish.
             sampled_surnames = [f"Surname{i}" for i in range(len(unique_cars))]

        # 7-qadam: 'owners' (Egalar) jadvalini yaratish.
        # Ikki ustundan iborat: CarNumber va SURNAME.
        owners = pd.DataFrame({
            'CarNumber': unique_cars,
            'SURNAME': sampled_surnames
        })
        
        # 8-qadam: Natijalarni saqlash.
        # index=False: faylga indeks raqamlarini yozmaslik.
        fines.to_csv('fines.csv', index=False)
        owners.to_csv('owners.csv', index=False)
        
        # Fayllar muvaffaqiyatli yaratilganligini tekshirish.
        if os.path.exists('fines.csv') and os.path.exists('owners.csv'):
            print("SUCCESS: Output files created.")
        
    except Exception as e:
        print(f"FAILURE: Exception occurred: {e}")

if __name__ == "__main__":
    verify()
