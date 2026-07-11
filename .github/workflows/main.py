import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

message = """
🏆 GOLD SIGNAL BOT

🟡 SIGNAL : WAIT

Bot berhasil berjalan di GitHub Actions.

Selanjutnya kita akan menambahkan:
✅ Harga Antam
✅ Buyback
✅ Buy / Wait / Sell
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message,
    },
)
