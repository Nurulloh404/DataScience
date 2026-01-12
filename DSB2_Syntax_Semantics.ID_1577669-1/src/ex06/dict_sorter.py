def dict_sorter():
        # Kortejlar ro'yxati (List of Tuples).
        # Har bir element ('Davlat nomi', 'Raqam sifatidagi satr') ko'rinishida.
        list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]

        # 1. Ro'yxatni Lug'atga aylantirish.
        countries_dict = {}
        for country, number in list_of_tuples:
            # int(number) - '25' kabi satrni 25 (butun son) ga aylantiradi.
            # Agar aylantirmasak, saralash satr bo'yicha ketadi ('100' < '2' bo'lib qoladi), bu noto'g'ri.
            countries_dict[country] = int(number)

        # 2. Lug'atni saralash (Sorting).
        # sorted() - Pythonning o'rnatilgan funksiyasi, ro'yxatni saralab yangi ro'yxat qaytaradi.
        
        # argument 1: countries_dict.items() -> [(Russia, 25), (France, 132)...] ro'yxatini beradi.
        
        # argument 2: key=lambda item: ... -> Saralash kaliti.
        # Lambda funksiya (nomsiz funksiya) sintaksisi: "lambda argumentlar: ifoda".
        # item - bu yerda har bir (Davlat, Raqam) juftligi.
        # item[0] = Davlat, item[1] = Raqam.
        
        # Bizga kerak:
        # 1-mezon: Raqam bo'yicha kamayish tartibida. "-item[1]" ishlatamiz, chunki Python odatda o'sish tartibida saralaydi.
        # Manfiy belgi qo'yilsa, katta sonlar kichik bo'lib qoladi, shuning uchun eng katta sonlar ro'yxat boshiga keladi.
        # 2-mezon: Agar raqamlar teng bo'lsa (masalan France va Germany 132), Davlat nomi bo'yicha alifbo tartibida. "item[0]".
        
        # Natijada qaytadigan qiymat: (-132, 'France'). Kortejlarni saralashda Python avval 1-elementga qaraydi, keyin 2-elementga.
        sorted_countries = sorted(countries_dict.items(), key=lambda item: (-item[1], item[0]))

        # 3. Natijani chiqarish.
        # sorted_countries endi saralangan kortejlar ro'yxati.
        for country, _ in sorted_countries:
            # country - Davlat nomi.
            # _ (pastki chiziq) - Keraksiz o'zgaruvchi. Bizga raqam kerak emas, faqat davlat nomi kerak.
            print(country)

if __name__ == '__main__':
    dict_sorter()
    