"""
Ushbu skript ('create_data.py') loyiha uchun zarur bo'lgan boshlang'ich ma'lumotlarni generatsiya qilish (yaratish) uchun xizmat qiladi.
U quyidagi vazifalarni bajaradi:
1.  `src/data` papkasini yaratadi (agar mavjud bo'lmasa).
2.  `feed-views.log` faylini yaratadi: bu foydalanuvchilarning saytga tashrifi (views) tarixini simulyatsiya qiluvchi log fayl.
3.  `auto.csv` faylini yaratadi: bu avtomobillar, jarimalar va to'lovlar haqidagi ma'lumotlarni o'z ichiga olgan jadval. Ma'lumotlar tozalash (cleaning) mashqlari uchun ataylab "iflos" (missing values, duplicates) holda yaratiladi.

Asosiy ishlatilgan kutubxonalar:
- `pandas`: Ma'lumotlar jadvallari (DataFrames) bilan ishlash va CSV fayllarni yaratish uchun.
- `numpy`: NaN (bo'sh qiymat) larni qo'shish va ba'zi matematik amallar uchun.
- `os`: Fayl tizimi (papka yaratish, fayl yo'llarini tekshirish) bilan ishlash uchun.
- `random`: Tasodifiy ma'lumotlar (sanalar, ismlar, raqamlar) generatsiya qilish uchun.
- `datetime`: Sanalar va vaqtlar bilan ishlash uchun.
"""

import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta

def create_data_dir():
    """
    Ma'lumotlar saqlanadigan 'src/data' papkasini yaratadi.
    os.path.exists() funksiyasi papka borligini tekshiradi.
    os.makedirs() funksiyasi esa papkani yaratadi.
    """
    if not os.path.exists('src/data'):
        os.makedirs('src/data')

def generate_feed_views():
    """
    'src/data/feed-views.log' faylini generatsiya qiladi.
    Bu fayl foydalanuvchilarning ko'rishlar tarixini ifodalaydi.
    """
    print("Generating src/data/feed-views.log...")
    # Foydalanuvchilar ro'yxati (bu ro'yxatdan tasodifiy tanlab olinadi)
    users = ['artem', 'oksana', 'ekaterina', 'maxim', 'valentina', 'pavel', 'anastasia']
    
    # 500 ta qator generatsiya qilish uchun tayyorgarlik
    dates = []
    # Boshlang'ich sana: 2020-yil 1-aprel
    base_date = datetime(2020, 4, 1)
    
    # 500 marta aylanish (sikl)
    for _ in range(500):
        # 2 oy (60 kun) ichida tasodifiy soniyalar miqdorini generatsiya qilish
        # 60 kun * 24 soat * 60 daqiqa * 60 soniya
        random_seconds = random.randint(0, 60*60*24*60)
        # Boshlang'ich sanaga tasodifiy soniyalarni qo'shib, yangi sana hosil qilish
        dates.append(base_date + timedelta(seconds=random_seconds))
    
    # Sanalarni vaqt o'sish tartibida (xronologik) saralash
    dates.sort()
    
    # Har bir sana uchun users ro'yxatidan tasodifiy bitta foydalanuvchini tanlash
    selected_users = [random.choice(users) for _ in range(500)]
    
    # Pandas DataFrame (jadval) yaratish
    # 'datetime' va 'user' ustunlaridan iborat
    df = pd.DataFrame({'datetime': dates, 'user': selected_users})
    
    # Ma'lumotlarni CSV faylga saqlash.
    # index=False: indeks raqamlarini faylga yozmaslik.
    # header=False: ustun nomlarini (datetime, user) yozmaslik (log fayl formati uchun).
    df.to_csv('src/data/feed-views.log', index=False, header=False)
    
    print("Generated src/data/feed-views.log")

def generate_auto_csv():
    """
    'src/data/auto.csv' faylini generatsiya qiladi.
    Bu fayl avtomobillar, jarimalar va to'lovlar haqidagi ma'lumotlarni o'z ichiga oladi.
    Ma'lumotlarni tozalash (data cleaning) mashqlari uchun maxsus "iflos" ma'lumotlar (NaN, dublikatlar) qo'shiladi.
    """
    print("Generating src/data/auto.csv...")
    
    # Avtomobil modellari ro'yxati
    makes_models = [
        'Ford Focus', 'Toyota Camry', 'Skoda Octavia', 'Volkswagen Passat', 'Volkswagen Golf',
        'Ford Mondeo', 'Ford Fiesta', 'BMW 320'
    ]
    
    # Generatsiya qilinadigan qatorlar soni
    n_rows = 1000
    
    # Tasodifiy avtomobil raqamlari bazasini yaratish (200 ta unikal raqam)
    # Rus nomerlari formatiga o'xshash: Harf-Raqam-Harf-Harf-Region
    car_numbers_pool = [f"{random.choice('ABETKMHOPCTX')}{random.randint(100, 999)}{random.choice('ABETKMHOPCTX')}{random.choice('ABETKMHOPCTX')}{random.randint(10, 199)}RUS" for _ in range(200)]
    
    # Har bir qator (1000 ta) uchun pool dan tasodifiy avtomobil raqamini tanlash
    car_numbers = [random.choice(car_numbers_pool) for _ in range(n_rows)]
    
    # Modelni tanlash
    # random.random() > 0.1 sharti 90% ehtimollik bilan modelni tanlaydi, 
    # 10% ehtimollik bilan esa np.nan (Not a Number - bo'sh qiymat) ni beradi.
    # Bu keyinchalik missing values bilan ishlashni mashq qilish uchun kerak.
    make_model_col = [random.choice(makes_models) if random.random() > 0.1 else np.nan for _ in range(n_rows)]
    
    # Jarimalarni generatsiya qilish (500 dan 5000 gacha), 10% holatda bo'sh (NaN)
    fines = [random.randint(500, 5000) if random.random() > 0.1 else np.nan for _ in range(n_rows)]
    
    # Qaytarilgan to'lovlar (refund) (1 dan 10 gacha), 10% holatda bo'sh (NaN)
    refunds = [random.randint(1, 10) if random.random() > 0.1 else np.nan for _ in range(n_rows)]
    
    # ID ustuni yaratish (1 dan 1000 gacha)
    ids = range(1, n_rows + 1)
    
    # Barcha ma'lumotlarni birlashtirib DataFrame yaratish
    df = pd.DataFrame({
        'ID': ids,
        'CarNumber': car_numbers,
        'Make_n_Model': make_model_col,
        'Fines': fines,
        'Refund': refunds,
        'Bio': [np.nan] * n_rows # 'Bio' ustuni butunlay bo'sh (NaN), keyinchalik tashlab yuborishni (drop) sinash uchun
    })
    
    # Dublikat qatorlar qo'shish.
    # df.sample(50): mavjud DataFrame dan 50 ta tasodifiy qatorni oladi.
    # pd.concat: asosiy DataFrame ga shu 50 ta qatorni ulaydi.
    # ignore_index=True: indekslarni qaytadan ketma-ket raqamlaydi.
    df = pd.concat([df, df.sample(50)], ignore_index=True)
    
    # Yakuniy natijani CSV faylga saqlash
    # index=False: faylga indeks raqamlarini yozmaslik.
    df.to_csv('src/data/auto.csv', index=False)
    print("Generated src/data/auto.csv with ID and extra col")

if __name__ == "__main__":
    # Dastur to'g'ridan-to'g'ri ishga tushirilganda (import qilinmaganda)
    # barcha funksiyalarni ketma-ket bajaradi.
    create_data_dir()
    generate_feed_views()
    generate_auto_csv()
