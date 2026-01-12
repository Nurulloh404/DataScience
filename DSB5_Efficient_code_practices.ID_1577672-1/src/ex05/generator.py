#!/usr/bin/env python3
import sys
import resource
import time

def read_file(filename):
    """
    Bu GENERATOR funksiya.
    'yield' so'zi ishlatilgani uchun bu funksiya faylni birdaniga o'qimaydi.
    
    Qanday ishlaydi:
    1. Funksiya chaqirilganda iteratsiya boshlanadi.
    2. 'yield line' ga kelganda funksiya PAUZA ga tushadi va 'line' ni qaytaradi.
    3. Keyingi safar so'ralganda to'xtagan joyidan davom etadi.
    
    Foydasi: Xotirada bir vaqtning o'zida faqat BITTA qator turadi.
    """
    with open(filename, 'r') as f:
        for line in f:
            yield line

def main():
    # Argumentlar sonini tekshirish
    if len(sys.argv) != 2:
        print("Usage: ./generator.py <filename>")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    try:
        # Hozirgi process vaqtini olamiz (boshlanish vaqti)
        start_time = time.process_time()
        
        # Generatorni yaratamiz (bu yerda fayl o'qilmaydi, faqat tayyorlanadi)
        lines = read_file(filename)
        
        # Generator orqali faylni AYLANIB chiqamiz
        for _ in lines:
            pass # Faylni shunchaki o'qib chiqamiz, hech narsa qilmaymiz
        end_time = time.process_time()
        
        # Peak memory usage in KB (Linux) -> Convert to GB
        # getrusage(RUSAGE_SELF): Dasturning o'zi (SELF) ishlatgan resurslarni oladi.
        # ru_maxrss (Resident Set Size): Ishlatilgan maksimal operativ xotira (RAM).
        # Linuxda bu qiymat Kilabaytda (KB) qaytadi. Gigabaytga o'tish uchun 1024*1024 ga bo'lamiz.
        peak_memory_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        peak_memory_gb = peak_memory_kb / (1024 * 1024)
        
        cpu_time = end_time - start_time
        
        print(f"Peak Memory Usage = {peak_memory_gb:.3f} GB")
        print(f"User Mode Time + System Mode Time = {cpu_time:.2f}s")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
