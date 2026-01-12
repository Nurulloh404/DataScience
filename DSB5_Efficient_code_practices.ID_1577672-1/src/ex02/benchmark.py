#!/usr/bin/env python3
import timeit
import sys

def loop_method(emails):
    result = []
    for email in emails:
        if "@gmail.com" in email:
            result.append(email)
    return result

def comprehension_method(emails):
    return [email for email in emails if "@gmail.com" in email]

def map_method(emails):
    return list(map(lambda x: x if "@gmail.com" in x else None, emails))

def filter_method(emails):
    """
    Bu funksiya 'filter' funksiyasidan foydalanadi.
    filter(shart_funksiyasi, toplamis) -> Faqat True qaytargan elementlarni olib qoladi.
    
    lambda x: "@gmail.com" in x
    - 'x' bu email stringi.
    - Funksiya faqat True yoki False qaytaradi.
    - Agar True bo'lsa, 'filter' uni natijaga qo'shadi.
    """
    return list(filter(lambda x: "@gmail.com" in x, emails))

def main():
    # Dastur ishga tushganda argumentlar sonini tekshiramiz
    # sys.argv[0] - dastur nomi (benchmark.py)
    # sys.argv[1] - funksiya nomi (loop, map...)
    # sys.argv[2] - takrorlanishlar soni (times)
    # Jami 3 ta bo'lishi kerak.
    if len(sys.argv) != 3:
        print("Usage: ./benchmark.py <function> <times>")
        print("Functions: loop, list_comprehension, map, filter")
        return

    # Argumentlarni o'zgaruvchilarga olamiz
    function_name = sys.argv[1]
    try:
        # Ikkinchi argumentni butun songa (int) aylantiramiz
        times = int(sys.argv[2])
    except ValueError:
        print("Error: times must be an integer")
        return
        
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com','anna@live.com', 'philipp@gmail.com'] * 5
    
    try:
        # Foydalanuvchi qaysi funksiya nomini kiritganini tekshiramiz
        if function_name == "loop":
            # Agar "loop" bo'lsa, loop_method ni o'lchaymiz
            time = timeit.timeit(lambda: loop_method(emails), number=times)
        elif function_name == "list_comprehension":
            time = timeit.timeit(lambda: comprehension_method(emails), number=times)
        elif function_name == "map":
            time = timeit.timeit(lambda: map_method(emails), number=times)
        elif function_name == "filter":
            time = timeit.timeit(lambda: filter_method(emails), number=times)
        else:
            # Agar noma'lum nom kiritilgan bo'lsa
            print(f"Error: Unknown function '{function_name}'")
            return
            
        # Natijaviy vaqtni ekranga chiqarimiz
        print(time)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    