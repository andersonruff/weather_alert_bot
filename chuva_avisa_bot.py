import os
import requests
from datetime import datetime

# -------- CONFIGURAÇÕES --------
BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']
CITY = "Pouso Alegre"

# -------- FUNÇÃO TELEGRAM --------
def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

# -------- BUSCAR PREVISÃO --------
def get_weather():
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}&lang=pt"
    return requests.get(url).json()

# -------- EXECUÇÃO --------
if __name__ == "__main__":
    data = get_weather()

    condition = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]

    message = (
        f"🌦️ Previsão do Tempo\n\n"
        f"Cidade: {CITY}\n"
        f"Condição: {condition}\n"
        f"🌡️ Temperatura: {temp}°C\n"
        f"💧 Umidade: {humidity}%\n\n"
        f"⏰ {datetime.utcnow().strftime('%d/%m %H:%M UTC')}"
    )

    send_telegram(message)
    print("Mensagem enviada com sucesso!")
