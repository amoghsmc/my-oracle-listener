from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("📥 Received Alert:", data)

    # Extract values
    entry = data.get("entry")
    sl = data.get("sl")
    qty = data.get("qty")
    side = data.get("side")

    print(f"💼 Trade: {side.upper()} | Entry: {entry} | SL: {sl} | Qty: {qty}")
    
    # 🚀 Place order with exchange here if needed

    return jsonify({"status": "received"}), 200

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
