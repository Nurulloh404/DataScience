# MovieLens Analytics

Bu loyiha MovieLens ma'lumotlar to'plamini tahlil qilish uchun mo'ljallangan.

## Ishga tushirish

Loyihani ishga tushirish uchun quyidagi qadamlarni bajaring:

1. **Virtual muhit yaratish:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Kerakli kutubxonalarni o'rnatish:**

   ```bash
   pip install -r src/requirements.txt
   ```

3. **Tahlil skriptini ishga tushirish:**

   `movielens_analysis.py` fayli asosiy tahlil logikasini o'z ichiga oladi va uning ichida testlar ham mavjud.

   ```bash
   python3 src/movielens_analysis.py
   ```

4. **Hisobotni ko'rish:**

   `movielens_report.ipynb` fayli tahlil natijalarini ko'rsatuvchi Jupyter Notebook hisoblanadi.

   ```bash
   jupyter notebook src/movielens_report.ipynb
   ```

## Testlar

Loyihada yozilgan funksiyalarni tekshirish uchun `pytest` dan foydalanishingiz mumkin yoki to'g'ridan-to'g'ri skriptni ishga tushirishingiz mumkin (yuqorida ko'rsatilganidek).

```bash
pytest src/movielens_analysis.py
```
