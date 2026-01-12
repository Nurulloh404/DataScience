#!/usr/bin/env python3
import sys
import resource
import time

def read_file(filename):
    """
    Bu ODDIY funksiya.
    'readlines()' faylning HAMMA qatorlarini o'qib, bitta katta ro'yxatga (list) joylaydi.
    
    Muammo: Agar fayl 10 GB bo'lsa, ro'yxat ham 10 GB joy oladi.
    Bu holda kompyuterning xotirasi (RAM) to'lib qoladi va dastur qotib qolishi yoki o'chib ketishi mumkin.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def main():
    # Argumentlar sonini tekshirish
    if len(sys.argv) != 2:
        print("Usage: ./ordinary.py <filename>")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    try:
        # Boshlanish vaqtini belgilaymiz
        start_time = time.process_time()
        
        # Faylni to'liq o'qib, ro'yxatga olamiz (bu yerda xotira sarflanadi)
        lines = read_file(filename)
        
        # Ro'yxatni aylanib chiqamiz (shunchaki vaqt o'lchash jarayonini to'liq qilish uchun)
        for _ in lines:
            pass
        
        # Tugash vaqtini olamiz
        end_time = time.process_time()
        
        # Peak memory usage in KB (Linux) -> Convert to GB
        # getrusage returns KB on Linux, bytes on MacOS. Assuming Linux environment.
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
