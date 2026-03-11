import requests
from utils.headers import HEADERS
from utils.parser import clean_price

# 说明：抖音电商页面大多为动态渲染/反爬较强，
# 这里先给一个保底实现：请求页面后做简单的 HTML 解析。
# 如需更高成功率，建议接入官方/联盟 API、或用 playwright/selenium 抓取。

def get_price(url: str):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp.text, "lxml")

        # 尝试一些常见的价格选择器（命中率不保证）
        candidates = [
            {"id": "price"},
            {"class_": "price"},
            {"class_": "sale-price"},
            {"class_": "real-price"},
        ]

        text = ""
        for kw in candidates:
            node = soup.find(**kw)
            if node and node.get_text(strip=True):
                text = node.get_text(" ", strip=True)
                break

        p = clean_price(text) if text else ""
        if not p:
            return {
                "platform": "抖音电商",
                "url": url,
                "price": "",
                "status": "error",
                "msg": "未在静态HTML中解析到价格（可能为动态渲染/反爬）"
            }

        return {"platform": "抖音电商", "url": url, "price": p, "status": "ok"}
    except Exception as e:
        return {"platform": "抖音电商", "url": url, "status": "error", "msg": str(e)}
