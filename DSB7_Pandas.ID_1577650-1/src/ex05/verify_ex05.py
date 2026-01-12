"""
Ushbu skript ('verify_ex05.py') 05-mashq (Exercise 05) natijalarini tekshirish uchun yozilgan.
Mashqning maqsadi: Ma'lumotlar bilan ishlash samaradorligini (performance) va xotirani optimallashtirish (memory optimization) usullarini o'rganish.

Vazifalar:
1.  Jarayon vaqtini o'lchash (timing).
2.  Indekslash (indexing) yordamida qidiruvni tezlashtirish.
3.  Downcasting: Sonli ma'lumot turlarini kichikroq hajmga o'tkazish (masalan, float64 -> float32).
4.  Categorical data: Takrorlanuvchi matnli ma'lumotlarni 'category' turiga o'tkazish orqali xotirani tejash.

Ishlatilgan kutubxonalar:
- `pandas`: Ma'lumotlarni optimallashtirish va ishlash tezligini tekshirish uchun.
- `numpy`: Ma'lumot turlari (dtypes) bilan ishlash uchun.
- `time`: Dastur ishlash vaqtini o'lchash uchun (kodda bevosita ishlatilmasa ham, odatda shu maqsadda import qilinadi).
- `gc`: Garbage Collector (Keraksiz xotirani tozalash) uchun.
"""

import pandas as pd
import numpy as np
import time
import gc

def verify():
    """
    Ex05 mashqini tekshiruvchi asosiy funksiya.
    Ma'lumotlar bilan turli operatsiyalarni bajarish tezligini va xotirani optimallashtirish usullarini sinovdan o'tkazadi.
    """
    try:
        # 1-qadam: Ma'lumotlarni yuklash.
        # '../ex04/fines.csv' faylini o'qiymiz.
        df = pd.read_csv('../ex04/fines.csv')
        
        # 2-qadam: Hisoblash amalini tekshirish.
        # Vektorizatsiya: Pandas ustunlari ustida to'g'ridan-to'g'ri arifmetik amallar bajarish.
        # Bu for siklidan ko'ra ancha tez ishlaydi.
        # Yangi 'calculated' ustuni yaratilmoqda: Fines / Refund * Year
        df['calculated'] = df['Fines'] / df['Refund'] * df['Year']
        print(f"SUCCESS: Calculation successful. Sample: {df['calculated'].iloc[0]}")
        
        # 3-qadam: Indekslash va qidirish.
        # Maqsad: Muayyan avtomobil raqamini qidirish tezligini tekshirish.
        target_car = df['CarNumber'].iloc[0] # Birinchi mashinaning raqamini olamiz.
        
        # Boolean Indexing (Filtrlash):
        # 'CarNumber' ustuni 'target_car' ga teng bo'lgan barcha qatorlarni topish.
        match = df[df['CarNumber'] == target_car]
        print(f"SUCCESS: Indexing successful. Found {len(match)} rows.")
        
        # 4-qadam: Optimallashtirish - Downcasting (Hajmni kichraytirish).
        # Asl df ni buzmaslik uchun nusxa (copy) olamiz.
        optimized_df = df.copy()
        
        # 'float' (haqiqiy son) turidagi ustunlarni topish.
        # Odatda pandas 'float64' (8 bayt) ishlatadi.
        cols_float = optimized_df.select_dtypes(include=['float']).columns
        
        # pd.to_numeric(..., downcast='float'):
        # Ustunlardagi sonlarni iloji boricha kichikroq turga (masalan 'float32' - 4 bayt) o'tkazadi.
        # Bu xotirani tejashga yordam beradi.
        optimized_df[cols_float] = optimized_df[cols_float].apply(pd.to_numeric, downcast='float')
        
        # Tekshirish: 'Fines' ustuni 'float32' ga o'tdimi?
        if optimized_df['Fines'].dtype == 'float32':
             print("SUCCESS: Fines downcasted to float32.")
        else:
             print(f"INFO: Fines dtype: {optimized_df['Fines'].dtype}")
             
        # 5-qadam: Optimallashtirish - Categorical Data (Kategoriyalar).
        # 'object' (matn/string) turidagi ustunlarni topish.
        cols_obj = optimized_df.select_dtypes(include=['object']).columns
        
        for col in cols_obj:
            # Har bir matnli ustunni 'category' turiga o'tkazish.
            # Agar ustunda takrorlanuvchi qiymatlar (masalan, Marka nomlari) ko'p bo'lsa, 
            # 'category' turi xotirani sezilarli darajada tejaydi.
            optimized_df[col] = optimized_df[col].astype('category')
        
        # Tekshirish: 'Make' ustuni 'category' turiga o'tdimi?
        if optimized_df['Make'].dtype.name == 'category':
            print("SUCCESS: Make converted to category.")
        
        # 6-qadam: Xotirani tozalash.
        # Katta DataFrame lar bilan ishlaganda xotirani bo'shatish muhim.
        del df
        del optimized_df
        # gc.collect(): Python'ning "Garbage Collector"ini majburan ishga tushirish.
        gc.collect()
        
    except Exception as e:
        print(f"FAILURE: Exception occurred: {e}")

if __name__ == "__main__":
    verify()
