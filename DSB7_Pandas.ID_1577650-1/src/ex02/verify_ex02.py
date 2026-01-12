import pandas as pd
import numpy as np
import os

def verify():
    """
    Ex02 mashqini tekshiruvchi funksiya.
    Bu funksiya 'pandas' kutubxonasining turli metodlaridan foydalanib, ma'lumotlarni tozalash jarayonini amalga oshiradi.
    """
    try:
        # pd.read_csv: Pandas kutubxonasining funksiyasi.
        # Vazifasi: CSV formatidagi faylni o'qib, uni DataFrame (jadval) ko'rinishiga o'tkazadi.
        # 'index_col' parametri orqali 'ID' ustuni qatorlarning indeksi (identifikatori) sifatida belgilanmoqda.
        df = pd.read_csv('../data/auto.csv', index_col='ID')
        
        # df.shape: DataFrame'ning atributi (xususiyati).
        # U jadvalning o'lchamini (qatorlar soni, ustunlar soni) ko'rinishida qaytaradi.
        # [0] indeksi orqali faqat qatorlar soni olinmoqda.
        initial_count = df.shape[0]
        
        # pf.drop_duplicates: Pandas DataFrame metodi.
        # Vazifasi: Takrorlanuvchi (dublikat) qatorlarni o'chirib tashlaydi.
        # 'subset' parametri: faqat ko'rsatilgan ustunlar ('CarNumber', 'Make_n_Model', 'Fines') bo'yicha dublikatlarni qidiradi.
        # keep='last': takrorlangan qatorlarning eng oxirgisini saqlab qoladi, qolganlarini o'chiradi.
        df = df.drop_duplicates(subset=['CarNumber', 'Make_n_Model', 'Fines'], keep='last')
        dedup_count = df.shape[0]
        
        # Ma'lumotlardagi bo'sh qiymatlarni (NaN - Not a Number) tekshirish qismi.
        cols_before = df.columns
        
        # thresh parametri uchun hisob:
        # Bizga shunday ustunlar kerakki, ularda to'liq qiymatlar soni (Jami qator - 500) dan kam bo'lmasin.
        # Ya'ni, agar ustunda 500 dan ortiq bo'sh qiymat (NaN) bo'lsa, u ustun o'chiriladi.
        thresh = df.shape[0] - 500
        
        # df.dropna: Pandas DataFrame metodi.
        # Vazifasi: Bo'sh qiymat (NaN) mavjud bo'lgan qator yoki ustunlarni o'chiradi.
        # axis=1: Ustunlarni o'chirishni bildiradi (axis=0 bo'lsa qatorlar o'chirilardi).
        # thresh=thresh: Kamida 'thresh' ta to'liq (NaN bo'lmagan) qiymatga ega ustunlarni qoldiradi.
        df = df.dropna(thresh=thresh, axis=1)
        cols_after = df.columns
        
        if 'Bio' in cols_before and 'Bio' not in cols_after:
            print("SUCCESS: Bio column dropped.")
        else:
            print(f"INFO: Bio column handling: Before={cols_before}, After={cols_after}")
            
        # df.fillna: Pandas DataFrame metodi.
        # Vazifasi: Bo'sh qiymatlar (NaN) o'rnini to'ldiradi.
        # method='ffill' (forward fill): Bo'sh katakdan oldingi turgan qiymatni nusxalab, bo'sh joyga yozadi.
        df['Refund'] = df['Refund'].fillna(method='ffill')
        
        # df.mean(): Pandas Series metodi.
        # Vazifasi: 'Fines' ustunidagi barcha qiymatlarning o'rtacha arifmetigini hisoblaydi.
        mean_fines = df['Fines'].mean()
        
        # Bu yerda yana fillna metodi ishlatilmoqda, lekin endi aniq bir qiymat (o'rtacha qiymat) bilan to'ldiriladi.
        df['Fines'] = df['Fines'].fillna(mean_fines)
        
        # Funksiya: 'Make_n_Model' ustunidagi qiymatni (masalan "Ford Focus") ikkiga: Marka ("Ford") va Model ("Focus") ga ajratish uchun.
        # Bu funksiya keyinchalik .apply() metodi orqali har bir qatorga qo'llaniladi.
        def split_make_model(val):
            # 1-qadam: Qiymat mavjudligini tekshirish.
            # pd.isna(val) - Pandas funksiyasi bo'lib, agar 'val' qiymati NaN (Not a Number - bo'sh) bo'lsa, True qaytaradi.
            if pd.isna(val):
                # Agar qiymat yo'q bo'lsa, natija ham ikkita bo'sh (NaN) qiymatdan iborat Series bo'lishi kerak.
                return pd.Series([np.nan, np.nan])
            
            # 2-qadam: Matnni ajratish.
            # val.split(' ', 1) - Bu Pythonning standart string (matn) metodi.
            # ' ' - ajratuvchi belgi (probel).
            # 1 - maksimal ajratishlar soni. Ya'ni faqat birinchi probeldan keyin ajratiladi. 
            # Masalan: "Volkswagen Passat" -> ["Volkswagen", "Passat"]
            # Agar "Lada Vesta Cross" bo'lsa -> ["Lada", "Vesta Cross"] (faqat birinchi probel hisobga olinadi)
            parts = val.split(' ', 1)
            
            # 3-qadam: Natijani tekshirish va qaytarish.
            if len(parts) == 2:
                # Agar muvaffaqiyatli ikkiga ajralgan bo'lsa (Marka va Model mavjud),
                # ular Pandas Series obyekti sifatida qaytariladi.
                # Series qaytarilishi sababi: apply() metodi natijani DataFrame'ning ikkita ustuniga ("Make", "Model") joylashi uchun.
                return pd.Series([parts[0], parts[1]])
            else:
                # Agar faqat bitta so'z bo'lsa (probel yo'q bo'lsa), u Marka deb hisoblanadi, Model esa bo'sh (NaN) bo'ladi.
                return pd.Series([parts[0], np.nan])

        # df.apply: Pandas DataFrame/Series metodi.
        # Vazifasi: Funksiyani (split_make_model) ustunning har bir elementiga qo'llaydi.
        # Natijani ikkita yangi 'Make' va 'Model' ustunlariga yozadi.
        df[['Make', 'Model']] = df['Make_n_Model'].apply(split_make_model)
        
        # df.drop: Pandas DataFrame metodi.
        # Vazifasi: Ko'rsatilgan ustunni ('Make_n_Model') jadvaldan o'chirib tashlaydi.
        df = df.drop(columns=['Make_n_Model'])
        
        # df.to_json: Pandas DataFrame metodi.
        # Vazifasi: DataFrame ma'lumotlarini JSON formatidagi faylga yozadi.
        # orient='records': JSON tuzilishini [{}, {}, ...] ko'rinishida, ya'ni har bir qator alohida obyekt bo'lishini ta'minlaydi.
        df.to_json('auto.json', orient='records')
        
        if os.path.exists('auto.json'):
            print("SUCCESS: auto.json created.")
        
    except Exception as e:
        print(f"FAILURE: Exception occurred: {e}")

if __name__ == "__main__":
    verify()
