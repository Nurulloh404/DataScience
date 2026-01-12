def to_dictionary():
    # Kortejlar ro'yxati (List of Tuples).
    # Bu ma'lumotlar strukturasi [(A, B), (C, D)] ko'rinishida.
    # Har bir element - bu 2 ta qiymatdan iborat o'zgarmas kortej (tuple).
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

    # Bo'sh lug'at (dictionary) yaratamiz.
    country_dict = {}
    
    # Ro'yxatni aylanib chiqish (Iteratsiya).
    # 'Unpacking' (qutidan chiqarish) mexanizmi:
    # list_of_tuples ichidagi har bir element (kortej) ikkita o'zgaruvchiga bo'lib olinadi:
    # country = 1-element (masalan, 'Russia'), number = 2-element (masalan, '25').
    for country, number in list_of_tuples:
        # 'in' operatori: Kalit lug'atda mavjudligini tekshiradi.
        if number in country_dict:
            # Agar bu raqam allaqachon kalit sifatida bor bo'lsa:
            # Demak qiymat ro'yxat (list) bo'lishi kerak.
            # .append() metodi ro'yxat oxiriga yangi element qo'shadi.
            country_dict[number].append(country)
        else:
            # Agar raqam birinchi marta uchrayotgan bo'lsa:
            # Yangi kalit hosil qilamiz va uning qiymati sifatida 
            # Bitta elementdan iborat yangi ro'yxat ([country]) beramiz.
            # Eslatma: Shunchaki "country_dict[number] = country" deb yozsak, keyinchalik append qila olmaymiz (string bo'lib qoladi).
            country_dict[number] = [country]

    # Natijani chiqarish bosqichi.
    # .items() metodi lug'atdagi (kalit, qiymat) juftliklarini qaytaradi.
    for number, countries in country_dict.items():
        # 'countries' bu yerda ro'yxat (list).
        # Masalan: ['Russia', 'Brazil'] (chunki ikkalasining raqami 25).
        # Ichki tsikl (Nested loop) orqali ushbu ro'yxat ichidagi har bir davlatni olamiz.
        for country in countries:
            # String formatting.
            print(f"'{number}' : '{country}'")


if __name__ == '__main__':
    to_dictionary()