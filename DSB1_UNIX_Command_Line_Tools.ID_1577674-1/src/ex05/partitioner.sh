#!/bin/sh

# Kiruvchi fayldan sarlavhani o'qib olish.
HEADER=$(head -n 1 ../ex03/hh_positions.csv)

# Faylni awk yordamida qayta ishlash.
# -F,: Maydon ajratuvchisini vergul qilib belgilash.
# -v header="$HEADER": Shell o'zgaruvchisini awk o'zgaruvchisiga o'tkazish.
tail -n +2 ../ex03/hh_positions.csv | awk -F, -v header="$HEADER" '{
    # $2 bu created_at ustuni (masalan, "2020-04-11T...").
    # match: 2-ustunda YYYY-MM-DD shablonini qidirish.
    match($2, /[0-9]{4}-[0-9]{2}-[0-9]{2}/)
    
    # substr: Topilgan matnni ajratib olish.
    # RSTART: Moslik boshlangan indeks. RLENGTH: Moslik uzunligi.
    date_str = substr($2, RSTART, RLENGTH)
    
    # Fayl nomini yasash, masalan "2020-04-11.csv".
    filename = date_str ".csv"
    
    # Agar bu fayl nomini hali ko'rmagan bo'lsak, unga sarlavhani yozamiz.
    # seen[filename] 0 (yolg'on) dan boshlanadi, inkrementdan keyin 1 (rost) bo'ladi.
    if (!seen[filename]++) {
        print header > filename
    }
    
    # Joriy qatorni ($0) faylga qo'shish.
    print $0 >> filename
}'
