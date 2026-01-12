#!/bin/sh

# FILES: Sana bo'yicha CSV fayllarni topish uchun shablon (glob). Masalan 2024...csv
FILES="20*.csv"
OUT="hh_positions.csv"

# set -- $FILES: Fayllar ro'yxatini pozitsion parametrlarga ($1, $2...) o'rnatadi.
# Bu fayllar haqiqatan ham mavjudligini tekshirish uchun xavfsiz usul.
set -- $FILES
if [ ! -e "$1" ]; then
    echo "Birlashtirish uchun CSV fayllar topilmadi."
    exit 1
fi

# head -n 1 "$1" > "$OUT": Birinchi fayldan sarlavhani olib, chiquvchi faylga yozish.
head -n 1 "$1" > "$OUT"

# Barcha mos keluvchi fayllar bo'yicha sikl.
for f in $FILES; do
    # tail -n +2: Har bir faylning sarlavhasini tashlab o'tish (2-qatordan boshlash).
    # >>: Ma'lumotni chiquvchi fayl oxiriga qo'shish.
    tail -n +2 "$f" >> "$OUT"
done
