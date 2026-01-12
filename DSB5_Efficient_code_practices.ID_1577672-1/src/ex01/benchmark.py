import timeit


def loop_method(emails):
    result = []
    for email in emails:
        if "@gmail.com" in email:
            result.append(email)
    return result

def comprehension_method(emails):
    return [email for email in emails if "@gmail.com" in email]

def map_method(emails):
    """
    Bu funksiya 'map' funksiyasidan foydalanadi.
    map(funksiya, toplamis) -> Har bir elementga funksiyani qo'llaydi.
    
    lambda x: x if "@gmail.com" in x else None
    - Bu "lambda" funksiya. Uni bir qatorlik funksiya deb tushuning.
    - 'x' bu kiruvchi argument (email).
    - if/else: Agar gmail bo'lsa o'zini qaytaradi, bo'lmasa None qaytaradi.
    
    list(...): map aslida 'map object' qaytaradi, uni ro'yxatga o'girib olamiz.
    """
    return list(map(lambda x: x if "@gmail.com" in x else None, emails))

def main():
    # Test uchun email ro'yxatini yaratamiz va uni 5 barobar ko'paytiramiz
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com','anna@live.com', 'philipp@gmail.com'] * 5
    
    # Har bir funksiya necha marta takrorlanishi kerakligini belgilaymiz
    iterations = 1000000
    try:
        # Har bir funksiya uchun vaqtni o'lchaymiz:
        # 1. Loop usuli
        t_loop = timeit.timeit(lambda: loop_method(emails), number=iterations)
        # 2. List Comprehension usuli
        t_comp = timeit.timeit(lambda: comprehension_method(emails), number=iterations)
        # 3. Map usuli
        t_map = timeit.timeit(lambda: map_method(emails), number=iterations)
        
        # Qaysi biri eng tez ekanligini aniqlash uchun solishtiramiz:
        if t_loop <= t_comp and t_loop <= t_map:
            print("it is better to use a loop")
        elif t_map <= t_comp and t_map <= t_loop:
            print("it is better to use a map")
        else:
            print("it is better to use a list comprehension")
            
        # Uchala vaqtni tartiblaymiz va ekranga chiqarames
        times = sorted([t_map, t_loop, t_comp])
        print(f"{times[0]} vs {times[1]} vs {times[2]}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()
    