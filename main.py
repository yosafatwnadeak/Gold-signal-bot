import os
import requests

from goldvision.antam import get_antam_price

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

status = get_antam_price()

message = f"""
🏆 GoldVision

🔍 Status Koneksi Antam

HTTP Status : {status}

✅ Bot berhasil mengambil halaman website Antam.

Powered by GoldVision
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message,
    },
)
