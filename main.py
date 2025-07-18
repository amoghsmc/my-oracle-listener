from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8068558939:AAHcsThdbt0J1uzI0mT140H9vJXbcaVZ9Jk"
TELEGRAM_CHAT_ID = "871704959"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.ok

@app.route('/', methods=['GET'])
def home():
    return '✅ Oracle Listener is Live!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = f"🚨 Webhook received:\n{data}"
    success = send_telegram_message(message)
    return jsonify({"status": "sent" if success else "failed", "received": data}), 200
