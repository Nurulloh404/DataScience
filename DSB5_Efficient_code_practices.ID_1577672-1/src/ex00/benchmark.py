import timeit


def loop_method(emails):
    """
    Bu funksiya 'for' sikli yordamida ro'yxatni aylanib chiqadi.
    Agar element ichida '@gmail.com' bo'lsa, uni yangi ro'yxatga qo'shadi.
    Bu an'anaviy va oddiy usul.
    """
    result = []
    for email in emails:
        if "@gmail.com" in email:
            result.append(email)
    return result

def comprehension_method(emails):
    """
    Bu funksiya 'List Comprehension' usulidan foydalanadi.
    Bu usul 'loop' usuliga qaraganda qisqaroq va odatda tezroq ishlaydi.
    
    Tuzilishi: [ <natija> for <element> in <toplam> if <shart> ]
    - <natija>: natijaviy ro'yxatga tushadigan narsa (bu yerda 'email')
    - <element>: har bir qadamdagi o'zgaruvchi
    - <toplam>: qayerdan olinayotgani (bu yerda 'emails' ro'yxati)
    - <shart>: qachon olinishi kerakligi (bu yerda '@gmail.com' bo'lsa)
    """
    return [email for email in emails if "@gmail.com" in email]

def main():
    # Ro'yxatni sun'iy ravishda ko'paytiramiz (benchmark aniqroq bo'lishi uchun)
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com','anna@live.com', 'philipp@gmail.com'] * 5
    try:
        # timeit.timeit: Funksiyani ko'p marta ishlatib ko'rib, ketgan vaqtni o'lchaydi.
        # lambda: Bu nomsiz funksiya. timeit argument sifatida funksiya kutadi, 
        # shuning uchun biz funksiyamizni (loop_method) lambda ichiga o'rab beramiz.
        # number=90000000: Funksiya shuncha marta (90 million) takrorlanadi.
        t_loop = timeit.timeit(lambda: loop_method(emails), number=90000000)
        
        # Xuddi shunday comprehension usuli uchun ham vaqtni o'lchaymiz
        t_comp = timeit.timeit(lambda: comprehension_method(emails), number=90000000)
        print(f"Loop method: {t_loop}")
        print(f"Comprehension method: {t_comp}")
        # timeit natijasi (sekundlarda) solishtirilmoqda
        # Agar loop tezroq bo'lsa:
        if t_loop < t_comp:
            print("it is better to use a loop")
        else:
            # Aks holda (comprehension tezroq bo'lsa):
            print("it is better to use a list comprehension")
            
        # Ikkala vaqtni ro'yxatga solib, o'sish tartibida saralaymiz (kichigi oldin)
        times = sorted([t_loop, t_comp])
        
        # Natijalarni ekranga chiqaramiz: eng tezi vs eng sekini
        print(f"{times[0]} vs {times[1]}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()
    