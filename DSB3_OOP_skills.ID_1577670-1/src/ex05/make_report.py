from analytics import Research, Analytics, Calculations
import config

def main():
    try:
        # 1. Ma'lumotlarni o'qish (Research klassi orqali)
        research = Research("data.csv")
        data = research.file_reader()
        
        # 2. Analytics obyektini yaratish va hisob-kitoblar
        analytics = Analytics(data)
        heads, tails = analytics.counts()
        p_heads, p_tails = analytics.fractions(heads, tails)
        
        # 3. Bashorat qilish
        forecast = analytics.predict_random(config.num_of_steps)
        # Bashorat natijasini hisoblash uchun Calculations klassidan foydalanamiz
        forecast_calc = Calculations(forecast)
        f_heads, f_tails = forecast_calc.counts()

        # 4. Hisobot matnini shakllantirish
        report = config.report_template.format(
            total=heads + tails,
            tails=tails,
            heads=heads,
            prob_tails=round(p_tails * 100, 2),
            prob_heads=round(p_heads * 100, 2),
            forecast_steps=config.num_of_steps,
            forecast_tails=f_tails,
            forecast_heads=f_heads
        )
        print(report)

        # 5. Faylga saqlash
        analytics.save_file(report, config.file_name, config.extension)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()