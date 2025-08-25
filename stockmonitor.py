import requests
import time
import yfinance as yf

BOT_TOKEN = "8389272178:AAHNwa_sDLarsFrAoSNhI54z4rifs8aQXMg"
CHAT_ID = "2065960507"
SYMBOL = "AAPL"  # Stock symbol to monitor
THRESHOLD = 200  # Alert price

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def get_price():
    ticker = yf.Ticker(SYMBOL)
    data = ticker.history(period="1m")
    return data["Close"].iloc[-1]

send_message(f"Started monitoring {SYMBOL} 📈")

while True:
    try:
        price = get_price()
        print(f"{SYMBOL} Current Price: {price}")
        if price > THRESHOLD:
            send_message(f"ALERT 🚀 {SYMBOL} crossed {THRESHOLD}! Current Price: {price}")
        time.sleep(60)
    except Exception as e:
        print("Error:", e)
        time.sleep(60)
