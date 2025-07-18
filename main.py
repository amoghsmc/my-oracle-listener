from flask import Flask, request

app = Flask(__name__)

# ✅ Add this route to handle homepage requests
@app.route("/", methods=["GET", "HEAD"])
def home():
    return "✅ Oracle Listener Running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📩 Webhook received:", data)
    return "✅ Webhook received successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
