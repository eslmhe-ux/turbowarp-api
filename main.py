from flask import Flask, Response
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

# لینک Raw گیت‌هاب گیست خودت رو اینجا بزار
GIST_RAW_URL = "https://gist.githubusercontent.com/eslmhe-ux/f604d4792869cca4dd1eb8c8a8e82f54/raw/9a0c842faf56cbeb4ffb619110ad1f2e91558c07/message.txt"

@app.route("/daily")
def get_daily():
    try:
        # دریافت متن زنده از Gist با جلوگیری از کش شدن (Cache-Busting)
        res = requests.get(GIST_RAW_URL, params={"_t": os.urandom(4).hex()}, timeout=5)
        text = res.text
    except Exception as e:
        text = "خطا در دریافت پیام روز!"
    
    return Response(text, mimetype="text/plain; charset=utf-8")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
