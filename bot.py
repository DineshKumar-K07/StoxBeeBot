import requests

TOKEN = "8389272178:AAHNwa_sDLarsFrAoSNhI54z4rifs8aQXMg"
CHAT_ID = 2065960507  # Your chat_id
TEXT = "StockBot Connected Successfully! 🚀"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {"chat_id": CHAT_ID, "text": TEXT}

res = requests.get(url, params=params)
print(res.json())
