#!/usr/bin/env python3
import timeit
import random
from collections import Counter

def my_count(nums):
    """
    Bu funksiya elementlarni qo'lda sanaydi.
    Dict ochib, har bir son necha marta qatnashganini yozib boradi.
    """
    counts = {}
    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    return counts

def my_top(nums):
    """
    Bu funksiya eng ko'p uchragan 10 ta elementni topadi.
    1. Avval sanab chiqadi (my_count).
    2. Keyin qiymati bo'yicha kamayish tartibida saralaydi (sorted).
    
    sorted(..., key=lambda item: item[1], reverse=True)
    - key: nimaga asoslanib saralash kerak? 'item[1]' ya'ni qiymati bo'yicha (soni bo'yicha).
    - reverse=True: Bizga eng ko'plari kerak, shuning uchun kamayish tartibida (kattadan kichikka).
    
    3. Eng boshidagi 10 tasini qaytaradi ([:10]).
    """
    counts = my_count(nums)
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts[:10]

def counter_count(nums):
    """
    Bu funksiya Python'ning maxsus 'Counter' sinfidan foydalanadi.
    Counter - bu C tilida yozilgan va optimallashtirilgan lug'at (dictionary).
    U oddiy for-siklga qaraganda ancha tez ishlaydi.
    """
    return Counter(nums)

def counter_top(nums):
    """
    Counter'ning o'zida 'most_common' degan maxsus metod bor.
    Bu eng ko'p uchragan elementlarni topishning eng samarali yo'li.
    """
    return Counter(nums).most_common(10)

def main():
    # Tasodifiy sonlar generatorini "muzlatib" qo'yamiz (har doim bir xil sonlar chiqishi uchun)
    random.seed(42)
    # 0 dan 100 gacha bo'lgan sonlardan iborat 1 milliontalik ro'yxat tuzamiz
    nums = [random.randint(0, 100) for _ in range(1000000)]
    
    # 1. Qo'lda yozilgan 'my_count' funksiyasini 1 marta ishlatib ko'ramiz
    time_my_count = timeit.timeit(lambda: my_count(nums), number=1)
    # 2. Python'ning tayyor 'Counter' sinfini ishlatib ko'ramiz
    time_counter_count = timeit.timeit(lambda: counter_count(nums), number=1)
    
    # 3. Eng ko'p 10 ta elementni topish (qo'lda yozilgan)
    time_my_top = timeit.timeit(lambda: my_top(nums), number=1)
    # 4. Eng ko'p 10 ta elementni topish (Counter yordamida)
    time_counter_top = timeit.timeit(lambda: counter_top(nums), number=1)
    
    # Natijalarni (vaqtlarni) ekranga chiqaramiz
    print(f"my function: {time_my_count}")
    print(f"Counter: {time_counter_count}")
    print(f"my top: {time_my_top}")
    print(f"Counter's top: {time_counter_top}")

if __name__ == "__main__":
    main()