#!/bin/sh

# jq: JSON ma'lumotlarini qayta ishlovchi buyruqlar qatori vositasi.
# -r: Raw (xom) chiqish. Agar natija satr bo'lsa, u qo'shtirnoqsiz yoziladi.
# -f filter.jq: jq filtrini 'filter.jq' faylidan o'qiydi.
# ../ex00/hh.json: Kiruvchi JSON fayli.
# > hh.csv: Standart chiqishni (natijani) 'hh.csv' fayliga yo'naltiradi (saqlaydi).

jq -r -f filter.jq ../ex00/hh.json > hh.csv
