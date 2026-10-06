from flask import Flask, Response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # برای جلوگیری از خطای امنیتی در مرورگر

DAILY_MESSAGE = "پیام امروز: خوش آمدید به بازی!"

@app.route("/daily")
def get_daily():
    return Response(DAILY_MESSAGE, mimetype="text/plain; charset=utf-8")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
