import sys

def caesar():
    # Argumentlar soni aniq 4 ta bo'lishi kerak:
    # 1. Dastur nomi, 2. Amal (encode/decode), 3. Matn, 4. Siljish (shift).
    if len(sys.argv) != 4:
        raise Exception("Invalid number of arguments")

    action = sys.argv[1]
    text = sys.argv[2]
    
    # 'try-except' bloki 'shift' o'zgaruvchisini butun son ekanligini tekshirish uchun.
    try:
        # int() funksiyasi satrni butun songa aylantiradi.
        shift = int(sys.argv[3])
    except ValueError:
        # Agar satr son bo'lmasa (masalan "uch"), xatolik beriladi.
        raise Exception("Shift must be an integer")

    # .isascii() - Agar satrdagi barcha belgilar ASCII jadvaliga tegishli bo'lsa True qaytaradi.
    # Kirill yoki boshqa alifbolarni hozircha qo'llab-quvvatlamaymiz.
    if not text.isascii():
         raise Exception("The script does not support your language yet.")

    # Amal turini aniqlaymiz.
    if action == 'encode':
        # Kodlash (shifrlash) uchun siljish o'zgarishsiz qoladi.
        pass
    elif action == 'decode':
        # Dekodlash (deshifrlash) uchun siljishni teskarisiga o'zgartiramiz.
        # Masalan, 3 ta oldinga siljigan bo'lsa, qaytarish uchun 3 ta orqaga siljish kerak (-3).
        shift = -shift
    else:
        raise Exception("Invalid action. Use 'encode' or 'decode'.")

    result = []
    # Matnni harfma-harf aylanib chiqamiz.
    for char in text:
        # Kichik harflar bilan ishlash ('a' dan 'z' gacha).
        # Python'da harflarni taqqoslash ularning ASCII kodlari orqali amalga oshiriladi.
        if 'a' <= char <= 'z':
            # ord(char) - Belgining sonli (ASCII) kodini qaytaradi ('a' -> 97).
            # (ord(char) - 97) -> Harfning alifbodagi o'rnini (0-25) topamiz.
            # + shift -> Siljishni qo'shamiz.
            # % 26 -> Modulo (qoldiq) operatori. Agar yig'indi 25 dan oshsa, aylantirib yana boshiga qaytaradi.
            # + 97 -> Qayta ASCII kodga o'tkazamiz.
            shifted = (ord(char) - 97 + shift) % 26 + 97
            
            # chr() - Sonli kodni belgiga aylantiradi.
            # .append() - Ro'yxatga qo'shish.
            result.append(chr(shifted))
            
        # Katta harflar bilan ishlash ('A' dan 'Z' gacha).
        elif 'A' <= char <= 'Z':
            # 'A' ning kodi 65. Xuddi tepadagi mantiq, faqat baza 65.
            shifted = (ord(char) - 65 + shift) % 26 + 65
            result.append(chr(shifted))
        else:
            # Harf bo'lmagan belgilar (probel, !, ? va h.k.) o'zgarishsiz qoladi.
            result.append(char)

    # Natijaviy ro'yxatni bitta satrga birlashtiramiz.
    # "".join(['S', 'a', 'l', 'o', 'm']) -> "Salom"
    print("".join(result))

if __name__ == '__main__':
    caesar()
