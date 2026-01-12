import sys

def extract_names():
    # Argumentlar sonini tekshiramiz.
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")

    # Kirish fayli nomini (input_file) argumentdan olamiz.
    input_file = sys.argv[1]
    
    # Kirish faylini ('r' - read) ochib, barcha qatorlarni 'emails' ro'yxatiga o'qiymiz.
    with open(input_file, 'r') as f:
        emails = f.readlines()

    # 'employees.tsv' faylini ('w' - write) yozish rejimida ochamiz.
    with open('employees.tsv', 'w') as f:
        # Faylning birinchi qatoriga sarlavhalarni (Header) yozamiz.
        # \t - tabulyatsiya, \n - yangi qatorga o'tish.
        f.write('Name\tSurname\tEmail\n')
        
        # Har bir email satri bo'yicha iteratsiya qilamiz.
        for email in emails:
            # Satr boshidagi va oxiridagi bo'shliqlarni olib tashlaymiz.
            email = email.strip()
            # Agar bo'sh satr bo'lsa (if not email), uni o'tkazib yuboramiz (continue).
            if not email:
                continue
            
            try:
                # Emaildan ism va familiyani ajratib olishga harakat qilamiz.
                # Format: ism.familiya@kompaniya.com deb hisoblaymiz.
                
                # 1. str.split('@') - satrni '@' belgisi bo'yicha 2 ga bo'ladi.
                # [0]-index orqali birinchi qismni (ism.familiya) olamiz.
                local_part = email.split('@')[0]
                
                # 2. Endi local_partni '.' (nuqta) bo'yicha bo'lamiz.
                # Unpacking: Natijani to'g'ridan-to'g'ri 2ta o'zgaruvchiga yuklaymiz.
                name_part, surname_part = local_part.split('.')
                
                # 3. .capitalize() - Satrning faqat birinchi harfini katta qiladi (qolganlari kichik).
                # Masalan: 'nurulloh' -> 'Nurulloh'.
                name = name_part.capitalize()
                surname = surname_part.capitalize()
                
                # 4. Yakuniy formatlangan satrni faylga yozamiz.
                f.write(f'{name}\t{surname}\t{email}\n')
            
            except ValueError:
                # 'ValueError' xatoligi qachon chiqishi mumkin?
                # Masalan, 'local_part.split('.')' qilganda nuqta yo'q bo'lsa,
                # unpacking (2 ta o'zgaruvchiga bo'lish) ishlamaydi va xatolik beradi.
                # Bunday holatda 'continue' qilib, keyingi emailga o'tamiz.
                continue

if __name__ == '__main__':
    extract_names()
