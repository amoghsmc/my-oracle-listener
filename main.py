from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Telegram credentials
BOT_TOKEN = "8068558939:AAHcsThdbt0J1uzI0mT140H9vJXbcaVZ9Jk"
CHAT_ID = "871704959"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Format message
    signal = data.get("signal", "NO SIGNAL")
    price = data.get("price", "N/A")
    symbol = data.get("symbol", "N/A")
    message = f"🚨 Signal Received\n📈 {symbol} | {signal}\n💰 Price: {price}"

    # Send to Telegram
    response = requests.post(TELEGRAM_URL, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    if response.status_code == 200:
        return "✅ Webhook received successfully!"
    else:
        return "❌ Telegram error", 500

@app.route('/', methods=['GET'])
def home():
    return "👋 Webhook Listener is Live!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
