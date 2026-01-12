#!/bin/sh

# Sarlavhani (birinchi qatorni) ajratib olib, yangi faylga saqlash.
# head -n 1: Faylning birinchi 1 qatorini chiqaradi.
head -n 1 ../ex01/hh.csv > hh_sorted.csv

# Faylning qolgan qismini saralash va yangi faylga qo'shish.
# tail -n +2: Faylni 2-qatordan boshlab chiqaradi (sarlavhani tashlab o'tadi).
# |: 'tail' ning chiqishini 'sort' ning kirishiga bog'laydi (pipe).
# sort: Matnli fayl qatorlarini saralaydi.
# -t,: Maydon ajratuvchisi sifatida vergul ',' ni belgilaydi (chunki bu CSV).
# -k2,2: 2-ustun bo'yicha saralaydi (created_at).
# -k1,1: Agar 2-ustun qiymatlari teng bo'lsa, keyin 1-ustun (id) bo'yicha saralaydi.
# >>: Chiqishni 'hh_sorted.csv' fayliga qo'shadi (sarlavhani saqlagan holda).
tail -n +2 ../ex01/hh.csv | sort -t, -k2,2 -k1,1 >> hh_sorted.csv
