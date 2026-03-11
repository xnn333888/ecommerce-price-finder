import requests
from utils.headers import HEADERS
from utils.parser import clean_price

def get_price(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp.text, "lxml")
        price = soup.find(class_="p-price")
        p = clean_price(price.get_text()) if price else ""
        return {
            "platform": "京东",
            "url": url,
            "price": p,
            "status": "ok"
        }
    except Exception as e:
        return {"platform": "京东", "url": url, "status": "error", "msg": str(e)}