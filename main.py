from flask import Flask, request

app = Flask(__name__)

# ✅ Default home route to avoid 405 error
@app.route("/", methods=["GET"])
def home():
    return "✅ Oracle Listener is live and ready!"

# ✅ Your main TradingView webhook listener
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📩 Webhook received:", data)
    return "✅ Webhook received successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
