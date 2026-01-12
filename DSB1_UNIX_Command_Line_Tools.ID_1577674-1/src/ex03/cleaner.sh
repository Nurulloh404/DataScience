#!/bin/sh

# Bu script CSV ni qatorma-qator ishlash uchun vaqtinchalik Python skriptini yaratadi.
# Chunki shell/sed yordamida murakkab CSV larni (qo'shtirnoqlar bilan) tahlil qilish qiyin bo'lishi mumkin.

# cat << 'EOF' > cleaner.py: cleaner.py faylini yaratadi va EOF gacha bo'lgan matnni yozadi.
cat << 'EOF' > cleaner.py
import sys
import csv
import re

def clean_name(name):
    # re.findall: Matn ichidan aytilgan shablonda mos keluvchi barcha qismlarni topadi.
    # r'(Junior|Middle|Senior)': Ushbu 3 ta so'zdan birini qidiruvchi Regex guruhi.
    # re.IGNORECASE: Katta-kichik harflarni farqlamaslik rejimi.
    matches = re.findall(r'(Junior|Middle|Senior)', name, re.IGNORECASE)
    
    # Agar hech qanday moslik topilmasa, "-" qaytaradi.
    if not matches:
        return "-"
    
    # Topilgan so'zlarni bosh harf bilan yozib (masalan jUnIoR -> Junior), '/' bilan birlashtiradi.
    return "/".join([m.capitalize() for m in matches])

try:
    # Standart kirishdan (pipe orqali) o'qish va standart chiqishga yozish.
    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout)

    # Sarlavhani o'qish va o'zgarishsiz yozish.
    header = next(reader)
    writer.writerow(header)

    # 'name' ustunining indeksini aniqlash.
    try:
        name_idx = header.index("name")
    except ValueError:
        name_idx = 2  # Agar sarlavha topilmasa, standart bo'yicha 3-ustun (indeks 2) olinadi.

    # Har bir qatorni qayta ishlash
    for row in reader:
        if len(row) > name_idx:
            # Name ustunini tozalangan qiymatga o'zgartirish
            row[name_idx] = clean_name(row[name_idx])
        writer.writerow(row)

except Exception as e:
    sys.stderr.write(f"Xatolik: {e}\n")
    sys.exit(1)
EOF

# Python skriptini ishga tushirish.
# < : Kiruvchi faylni yo'naltirish.
# > : Natijani chiquvchi faylga yo'naltirish.
python3 cleaner.py < ../ex02/hh_sorted.csv > hh_positions.csv

# Vaqtinchalik python faylini o'chirish.
rm cleaner.py
