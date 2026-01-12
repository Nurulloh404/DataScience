# 'sys' - (System-specific parameters and functions) moduli.
# Bu modul orqali interpretator foydalanadigan o'zgaruvchilarga va funksiyalarga murojaat qilish mumkin.
import sys


def find_ticker_info(ticker_input):
    # 'COMPANIES' lug'ati (dict).
    # {} jingalak qavslar lug'atni bildiradi.
    # Har bir qator 'Kalit': 'Qiymat' ko'rinishida.
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    
    # 'STOCKS' lug'ati. Ticker nomi -> Narx.
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    found_ticker = None
    
    # Lug'at kalitlari bo'yicha iteratsiya.
    # 'ticker' o'zgaruvchisi har bir aylanishda navbatdagi kalitni (AAPL, MSFT va hokazo) oladi.
    for ticker in STOCKS:
        # String metodlari:
        # .lower() - barcha harflarni kichik harfga o'tkazadi.
        # Bu qidiruvni case-insensitive (katta-kichik harfga bog'liq bo'lmagan) qilish uchun kerak.
        if ticker.lower() == ticker_input.lower():
            # Agar moslik topilsa, asl ticker nomini (masalan 'AAPL') 'found_ticker' ga saqlaymiz.
            found_ticker = ticker
            
            # tsiklni shu zahoti to'xtatamiz.
            break

    # if sharti: Agar found_ticker o'zgaruvchisi bo'sh bo'lmasa (None bo'lmasa).
    if found_ticker:
        found_company = None
        
        # Lug'atning .items() metodi.
        # Bu metod lug'atdagi har bir juftlikni (Kalit, Qiymat) ko'rinishida qaytaradi.
        # 'name' - Kalitni oladi (Kompaniya nomi).
        # 'tick' - Qiymatni oladi (Ticker belgisi).
        for name, tick in COMPANIES.items():
            # Agar ushbu kompaniyaning tickeri biz qidirayotgan tickerga teng bo'lsa:
            if tick == found_ticker:
                found_company = name # Kompaniya nomini saqlab olamiz.
                break
        
        # Lug'atdan qiymat olish: Lug'atNomi[Kalit].
        price = STOCKS[found_ticker]
        
        # f-string (Formatlangan satr).
        # f"... {o'zgaruvchi} ..." ko'rinishida yoziladi va o'zgaruvchilar qiymati avtomatik joylanadi.
        print(f"{found_company} {price}")
    else:
        # Ticker topilmagan holat.
        print("Unknown ticker")


def main():
    # len() - obyektning uzunligini (elementlar sonini) o'lchaydi.
    # sys.argv ro'yxatini tekshiramiz.
    if len(sys.argv) == 2:
        # List index (Ro'yxat indeksi).
        # Ro'yxat elementlariga murojaat 0 dan boshlanadi.
        # sys.argv[0] - har doim dastur nomi.
        # sys.argv[1] - bizga kerak bo'lgan argument.
        find_ticker_info(sys.argv[1])


# Modulni tekshirish.
# Agar ushbu fayl to'g'ridan-to'g'ri ishga tushirilsa, __name__ == '__main__' bo'ladi.
# Agar boshqa fayldan 'import' qilinsa, __name__ fayl nomi bo'ladi.
if __name__ == '__main__':
    main()