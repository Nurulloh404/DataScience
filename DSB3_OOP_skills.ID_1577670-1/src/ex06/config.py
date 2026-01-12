# Bashorat qilinadigan qadamlar soni
num_of_steps = 3

# Hisobot shabloni
report_template = """Report:
We made {total} observations by tossing a coin: {tails} were tails and {heads} were heads.
The probabilities are {prob_tails}% and {prob_heads}%, respectively.
Our forecast is that the next {forecast_steps} observations will be: {forecast_tails} tail and {forecast_heads} heads."""

# Fayl nomi va kengaytmasi
file_name = "report"
extension = "txt"

# Log fayli
log_file = "analytics.log"

# Telegram sozlamalari
telegram_token = "8095689664:AAE1MNyI3UXh-E0t4jRRzilPU85Zhc6xfbo"
telegram_chat_id = "6267234682"

# Telegram xabarlari
success_msg = "The report has been successfully created"
fail_msg = "The report hasn't been created due to an error"