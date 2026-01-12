import sys

def marketing_tasks():
    # Ro'yxatlar (Lists). 
    # Bu yerda oddiy string (matn) elementlaridan iborat ro'yxatlar keltirilgan.
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
    ]
    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com'
    ]
    recipients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'
    ]

    # Argumentlarni tekshirish.
    # "!=" - "teng emas" operatori.
    if len(sys.argv) != 2:
        # Istisno (Exception) ko'tarish. Dastur shu joyda to'xtaydi va xatolik beradi.
        raise Exception("Invalid arguments")

    task = sys.argv[1]

    # 'set' (To'plam) ma'lumot turi.
    # To'plamning asosiy xususiyatlari:
    # 1. Takrorlanmas elementlar (har bir element faqat 1 marta qatnashadi).
    # 2. Tartibsiz (indeks orqali murojaat qilib bo'lmaydi).
    # 3. Matematik to'plamlar amallarini qo'llab-quvvatlaydi (birlashma, kesishma, ayirma).

    if task == 'call_center':
        # Vazifa: Mijoz bo'lgan, lekin hali reklama xati olmagan odamlarni topish.
        # Buning uchun 'Mijozlar' to'plamidan 'Xat olganlar' to'plamini ayiramiz.
        # set(clients) - mijozlar ro'yxatini to'plamga aylantiradi (dublikatlarni yo'qotadi).
        # set(recipients) - xat olganlarni to'plamga aylantiradi.
        # "-" operatori: A - B -> A da bor, lekin B da yo'q elementlar.
        # list(...) - Natijaviy to'plamni yana ro'yxatga aylantiramiz (chop etish uchun).
        result = list(set(clients) - set(recipients))
        
    elif task == 'potential_clients':
        # Vazifa: Tadbirda qatnashgan, lekin hali mijoz bo'lmaganlar (Potentsial mijozlar).
        # Ishtirokchilar - Mijozlar.
        result = list(set(participants) - set(clients))
        
    elif task == 'loyalty_program':
        # Vazifa: Mijoz bo'lgan, lekin tadbirda qatnashmaganlar (ularni jalb qilish kerak).
        # Mijozlar - Ishtirokchilar.
        result = list(set(clients) - set(participants))
        
    else:
        # Agar vazifa nomi noto'g'ri bo'lsa, xatolik beramiz.
        raise Exception("Invalid task name")

    # Natijani ekranga chiqaramiz.
    print(result)

if __name__ == '__main__':
    marketing_tasks()
