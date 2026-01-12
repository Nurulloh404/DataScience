import sys
# 'import' kalit so'zi tashqi modullarni (kutubxonalarni) dasturga yuklash uchun ishlatiladi.
# 'sys' - tizim bilan ishlash moduli (masalan, argumentlarni o'qish).


def find_stock_price(company_name):
    # Lug'at (dictionary) yaratish.
    # Kalit (key): 'Apple', Qiymat (value): 'AAPL'.
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    
    # Ikkinchi lug'at.
    # Kalit: 'AAPL', Qiymat: 287.73 (float son).
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    # 'found_key' o'zgaruvchisini 'None' (hech narsa) qiymati bilan initsializatsiya qilamiz.
    # Bu o'zgaruvchi keyinchalik topilgan kompaniya nomini saqlash uchun kerak.
    found_key = None
    
    # 'for' tsikli orqali COMPANIES lug'atining KALITLARINI (kompaniya nomlarini) aylanib chiqamiz.
    for company in COMPANIES:
        # Satrlarni solishtirish.
        # .lower() metodi satrni to'liq kichik harflarga o'tkazadi ('Apple' -> 'apple').
        # Bu foydalanuvchi 'APPLE', 'apple', 'ApPlE' deb yozsa ham topish imkonini beradi.
        if company.lower() == company_name.lower():
            # Agar moslik topilsa, lug'atdagi asl nomni (masalan 'Apple') saqlab olamiz.
            found_key = company
            
            # 'break' - tsiklni muddatidan oldin to'xtatish.
            # Kerakli narsani topdik, endi davom etishga hojat yo'q.
            break

    # 'if found_key:' sharti 'if found_key is not None:' bilan bir xil ma'noni anglatadi.
    # Agar found_key ga qiymat yozilgan bo'lsa (ya'ni None bo'lmasa), shart bajariladi.
    if found_key:
        # Lug'atdan qiymat olish sintaksisi: lug'at_nomi[kalit].
        # 1-qadam: Kompaniya nomi orqali tickerni (masalan 'AAPL') olamiz.
        ticker = COMPANIES[found_key]
        
        # 2-qadam: Ticker orqali STOCKS lug'atidan narxni olamiz.
        # Va uni 'print()' funksiyasi orqali ekranga chiqarammiz.
        print(STOCKS[ticker])
    else:
        # Agar kompaniya topilmasa (found_key hali ham None bo'lsa):
        print("Unknown company")


def main():
    # sys.argv - buyruq satri argumentlari ro'yxati (list).
    # sys.argv[0] - har doim ishga tushirilayotgan skript nomi bo'ladi.
    # sys.argv[1] - foydalanuvchi kiritgan birinchi argument.
    # len() - ro'yxat uzunligini (elementlar sonini) qaytaradi.
    if len(sys.argv) == 2:
        # Agar argumentlar soni to'g'ri bo'lsa (skript nomi + kompaniya nomi = 2 ta),
        # funksiyani chaqiramiz va 1-argumentni unga uzatamiz.
        find_stock_price(sys.argv[1])


# Dastur bevosita ishga tushirilganda main() funksiyasini chaqiramiz.
if __name__ == '__main__':
    main()