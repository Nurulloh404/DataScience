# Bashorat qilinadigan qadamlar soni
num_of_steps = 3

# Hisobot shabloni (placeholder'lar bilan)
# .format() ishlatish uchun {o'zgaruvchi_nomi} ko'rinishida yoziladi
report_template = """Report:
We made {total} observations by tossing a coin: {tails} were tails and {heads} were heads.
The probabilities are {prob_tails}% and {prob_heads}%, respectively.
Our forecast is that the next {forecast_steps} observations will be: {forecast_tails} tail and {forecast_heads} heads."""

# Fayl nomi va kengaytmasi
file_name = "report"
extension = "txt"