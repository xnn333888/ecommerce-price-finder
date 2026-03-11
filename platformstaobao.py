import requests
from utils.headers import HEADERS
from utils.parser import clean_price

def get_price(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp.text, "lxml")
        price = soup.find(class_="tm-price") or soup.find(class_="price-now")
        p = clean_price(price.get_text()) if price else ""
        return {
            "platform": "淘宝/天猫",
            "url": url,
            "price": p,
            "status": "ok"
        }
    except Exception as e:
        return {"platform": "淘宝/天猫", "url": url, "status": "error", "msg": str(e)}