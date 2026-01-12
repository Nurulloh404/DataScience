# Funksiya (function) ta'rifi. 'def' kalit so'zi funksiya yaratish uchun ishlatiladi.
# 'transform_line' - funksiyaning nomi.
# '(line)' - funksiya qabul qiladigan argument (parametr).
def transform_line(line):
    # 'inside_quotes' - o'zgaruvchisi bayroqcha (flag) vazifasini bajaradi.
    # Dastlabki qiymati False (yolg'on), ya'ni biz qo'shtirnoq ichida emasmiz.
    inside_quotes = False
    
    # Bo'sh satr yaratamiz, bu yerga natijani yozib boramiz.
    result = ""
    
    # 'for' tsikli (loop). 'line' satridagi har bir 'char' (belgi) uchun takrorlanadi.
    for char in line:
        # 'if' shart operatori. Agar belgi qo'shtirnoq (") bo'lsa:
        if char == '"':
            # 'not' operatori mantiqiy qiymatni teskarisiga o'zgartiradi (True -> False yoki aksincha).
            # Bu yerda holatni almashtiramiz: kirdik <-> chiqdik.
            inside_quotes = not inside_quotes
            
            # '+=' operatori satrga yangi belgi qo'shish (konkatenatsiya) uchun ishlatiladi.
            result += char
            
        # 'elif' (else if) - agar birinchi shart bajarilmasa, keyingi shartni tekshiradi.
        # "Agar belgi vergul bo'lsa VA biz qo'shtirnoq ichida BO'LMASAK":
        elif char == ',' and not inside_quotes:
            # Vergulni 'tab' (\t) belgisiga almashtiramiz (TSV formati uchun).
            result += '\t'
            
        # 'else' - yuqoridagi hech qaysi shart bajarilmasa:
        else:
            # Belgini o'zgarishsiz natijaga qo'shamiz.
            result += char
            
    # 'return' kalit so'zi funksiya natijasini qaytaradi.
    return result


def main():
    # 'open()' funksiyasi faylni ochish uchun ishlatiladi.
    # 1-argument: fayl nomi ('ds.csv').
    # 2-argument: rejim ('r' - read/o'qish, 'w' - write/yozish).
    # Fayl obyekti 'input_file' o'zgaruvchisiga saqlanadi.
    input_file = open("ds.csv", "r")
    
    # Chiqish faylini 'w' (yozish) rejimida ochamiz.
    # Agar fayl mavjud bo'lmasa, yaratiladi. Mavjud bo'lsa, ichidagi ma'lumot o'chib ketadi (overwrite).
    output_file = open("ds.tsv", "w")

    # Fayl obyekti bo'ylab iteratsiya qilish (aylanib chiqish).
    # Python faylni avtomatik ravishda qator-ma-qator o'qiydi.
    for line in input_file:
        # Har bir qatorni yuqorida yozgan funksiyamiz orqali o'zgartiramiz.
        transformed = transform_line(line)
        
        # Fayl obyektining .write() methodi orqali ma'lumotni faylga yozamiz.
        output_file.write(transformed)

    # Fayllar bilan ishlash tugagach, ularni .close() metodi bilan yopish SHART.
    # Bu tizim resurslarini bo'shatadi va ma'lumotlar to'liq saqlanishini ta'minlaydi.
    input_file.close()
    output_file.close()

# Dastur nuqtasi.
if __name__ == '__main__':
    main()