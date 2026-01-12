import sys
# 'sys' moduli dasturga argumentlar uzatish va tizim funksiyalaridan foydalanish uchun kerak.


def process_stocks(arg_string):
    # 'COMPANIES' lug'ati (dict). Kalit: Kompaniya nomi, Qiymat: Ticker belgisi.
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    # 'STOCKS' lug'ati. Kalit: Ticker belgisi, Qiymat: Aksiya narxi.
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    # Satrni bo'laklash (String Split).
    # 'arg_string' - bu vergul bilan ajratilgan bitta uzun satr (masalan "Apple, MSFT, Google").
    # .split(',') metodi vergul bor joylardan satrni qirqib, ro'yxat (list) hosil qiladi.
    expressions = arg_string.split(',')
    
    # 1. Validatsiya bosqichi.
    # Har bir ifodani tekshiramiz. Agar bo'sh ifoda mavjud bo'lsa (masalan "Apple,,MSFT" da o'rtada bo'sh),
    # dastur ishlashini to'xtatamiz.
    for expr in expressions:
        # .strip() - satrning boshi va oxiridagi bo'sh joylarni (probel, tab, enter) olib tashlaydi.
        # " not expr.strip()" degani - agar tozalangandan keyin satr bo'sh qolsa (ya'ni faqat probellar bo'lgan bo'lsa).
        if not expr.strip():
            # 'return' hech narsa qaytarmaydi, shunchaki funksiyadan chiqib ketadi.
            return

    # Dictionary Comprehension (Lug'at generatori).
    # Bu juda kuchli va qisqa yozish usuli.
    # Bizga Ticker -> Kompaniya nomi teskari lug'ati kerak.
    # {k: v ...} o'rniga {v: k ...} yozib, kalit va qiymat o'rnini almashtiryapmiz.
    TICKER_TO_COMPANY = {v: k for k, v in COMPANIES.items()}

    # 2. Qayta ishlash bosqichi.
    for expr in expressions:
        # Ortiqcha bo'sh joylarni olib tashlaymiz.
        query = expr.strip()
        
        found_company_key = None
        # Qidiruv 1: Kompaniya nomi bo'yicha.
        for company in COMPANIES:
            # Case-insensitive (katta-kichik harfga bog'liq bo'lmagan) solishtirish.
            if company.lower() == query.lower():
                found_company_key = company
                break
        
        found_ticker_key = None
        # Qidiruv 2: Ticker bo'yicha.
        # Agar kompaniya nomi topilmasa ham, ticker sifatida qidirib ko'ramiz
        # (yoki ikkalasini ham baribir tekshirishimiz mumkin, lekin bu yerda alohida).
        for ticker in STOCKS:
            if ticker.lower() == query.lower():
                found_ticker_key = ticker
                break

        # Natijalarni tekshirish va chiqarish.
        if found_company_key:
            # Agar kompaniya nomi topilgan bo'lsa:
            ticker = COMPANIES[found_company_key] # Tickerni olamiz.
            price = STOCKS[ticker] # Narxni olamiz.
            print(f"{found_company_key} stock price is {price}")
            
        elif found_ticker_key:
            # Agar ticker topilgan bo'lsa:
            company_name = TICKER_TO_COMPANY[found_ticker_key] # Teskari lug'atdan nomni olamiz.
            print(f"{found_ticker_key} is a ticker symbol for {company_name}")
            
        else:
            # Hech narsa topilmasa:
            print(f"{query} is an unknown company or an unknown ticker symbol")


def main():
    # Faqat 2 ta element bo'lishi kerak: [skript_nomi, "uzun,satr,argument"].
    if len(sys.argv) == 2:
        process_stocks(sys.argv[1])


if __name__ == '__main__':
    main()
