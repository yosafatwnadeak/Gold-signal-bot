import requests
from bs4 import BeautifulSoup


def get_antam_price():
    url = "https://www.logammulia.com/id/harga-emas-hari-ini"

    response = requests.get(url, timeout=30)

    soup = BeautifulSoup(response.text, "html.parser")

    return response.status_code
