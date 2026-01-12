#!/usr/bin/env python3
import timeit
import sys
from functools import reduce

def loop(num):
    """
    Bu funksiya oddiy sikl yordamida yig'indini hisoblaydi.
    i*i (kvadrat) ni avvalgi qiymatga qo'shib boradi.
    """
    for i in range(num):
        num = num + i * i
    return num
def reduce_sum(num):
    """
    Bu funksiya 'reduce' dan foydalanadi.
    reduce(funksiya, ketma-ketlik) -> Ketma-ketlikni bitta qiymatga 'siqadi'.
    
    lambda x, y: x + y*y
    - x: oldingi qadamdan chiqqan natija (yig'indi).
    - y: navbatdagi kelayotgan son.
    - Har qadamda: eski yig'indiga (x) yangi sonning kvadratini (y*y) qo'shadi.
    """
    return reduce(lambda x, y: x + y * y, range(num))
def main():
    # Argumentlarni olamiz: func_name (funksiya nomi), times (necha marta), num (qaysi songacha)
    func_name = sys.argv[1]
    times = int(sys.argv[2])
    num = int(sys.argv[3])
    
    # Kiritilgan funksiya nomiga qarab tegishlisini ishlatamiz
    if func_name == "loop":
        # loop funksiyasini 'times' marta ishlatib, vaqtini o'lchaymiz
        print(timeit.timeit(lambda: loop(num), number=times))
    elif func_name == "reduce":
        # reduce funksiyasini o'lchaymiz
        print(timeit.timeit(lambda: reduce_sum(num), number=times))
    else:
        print("Invalid function name")
if __name__ == "__main__":
    main()
    