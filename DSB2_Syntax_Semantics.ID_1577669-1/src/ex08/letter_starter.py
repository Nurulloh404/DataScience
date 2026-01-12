import sys

def start_letter():
    # Argumentlar sonini tekshirish.
    # Dastur nomi (sys.argv[0]) + 1 ta elektron pochta (sys.argv[1]).
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")

    # Kiritilgan elektron pochta manzilini o'zgaruvchiga olamiz.
    email_arg = sys.argv[1]
    
    # 'try-except' bloki - Xatoliklarni ushlab qolish va ularni boshqarish uchun ishlatiladi.
    # Biz 'try' ichidagi kodni bajarishga harakat qilamiz.
    try:
        # 'with open(...) as f' - Fayl bilan ishlashning eng xavfsiz usuli.
        # Bu 'Context Manager' deb ataladi. U faylni ochadi va blok tugagandan keyin
        # (yoki xatolik yuz bersa ham) faylni AVTOMATIK ravishda yopadi (f.close() shart emas).
        with open('employees.tsv', 'r') as f:
            # .readlines() - fayldagi barcha qatorlarni o'qib, ularni ro'yxat (list) shaklida qaytaradi.
            lines = f.readlines()
            
        found = False
        
        # 'lines[1:]' - Ro'yxatni kesish (Slicing).
        # 0-indeksdagi qator (Sarlavha: Name, Surname...) bizga kerak emas.
        # Shuning uchun 1-indeksdan boshlab oxirigacha olamiz.
        for line in lines[1:]: 
            # 1. .strip() - qator boshidagi va oxiridagi ko'rinmas belgilarni (masalan, yangi qator \n) olib tashlaydi.
            # 2. .split('\t') - qatorni tabulyatsiya (\t) belgisi bo'yicha bo'laklarga ajratadi.
            parts = line.strip().split('\t')
            
            # Agar qatorda kamida 3 ta ustun bo'lsa (Ism, Familiya, Email va h.k.):
            if len(parts) >= 3:
                name = parts[0]   # 0-ustun: Ism
                email = parts[2]  # 2-ustun: Email (taxminan)
                
                # Agar fayldagi email biz qidirayotgan emailga teng bo'lsa:
                if email == email_arg:
                    # Tabriknoma matnini shakllantiramiz va chiqaramiz.
                    print(f"Dear {name}, welcome to our team! We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                    
                    found = True
                    # Qidiruvni to'xtatamiz.
                    break
        
        # Agar qidiruv tugab, 'found' hali ham False bo'lsa (ya'ni email topilmasa):
        if not found:
             pass # 'pass' - hech narsa qilmaslik uchun buyruq (placeholder).

    # Agar 'try' blokida fayl topilmasa (FileNotFoundError xatoligi chiqsa):
    except FileNotFoundError:
        # Dastur qulab tushmasligi uchun chiroyli qilib xatolik xabarini chiqaramiz.
        raise Exception("employees.tsv not found")

if __name__ == '__main__':
    start_letter()
