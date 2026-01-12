#!/bin/sh

# CSV sarlavhasini yaratish.
echo '"name","count"' > hh_uniq_positions.csv

# Konveyer (pipeline) tushuntirishi:
# 1. tail -n +2: Kiruvchi CSV sarlavhasini tashlab o'tadi.
# 2. awk -F, '{print $3}': Vergul bilan ajratib, 3-ustunni (name) chiqaradi.
# 3. sort: Qatorlarni saralaydi. 'uniq' ishlashi uchun saralangan bo'lishi shart.
# 4. uniq -c: Noyob qatorlarni sanaydi. Chiqish formati: "  7 Junior".
# 5. sort -rn: Sonlarni saralaydi. -r teskari tartibda (kamayish), -n raqam bo'yicha.
# 6. awk '{print $2","$1}': Chiqishni "Soni Nomi" dan "Nomi,Soni" formatiga o'zgartiradi.
# >>: Natijani fayl oxiriga qo'shadi.

tail -n +2 ../ex03/hh_positions.csv | \
awk -F, '{print $3}' | \
sort | \
uniq -c | \
sort -rn | \
awk '{print $2","$1}' >> hh_uniq_positions.csv
