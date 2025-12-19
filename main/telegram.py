import requests

def send_telegram_message(text):
    TOKEN = "8560114166:AAFmaX87kuxfpdjmHhHNuBbjZGTyxLLyLV4"
    CHAT_ID = "-1003421440492."
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })
