from platforms import taobao, jd, pdd, douyin

def get_price(url: str):
    if "taobao.com" in url or "tmall.com" in url:
        return taobao.get_price(url)
    elif "jd.com" in url:
        return jd.get_price(url)
    elif "pinduoduo.com" in url or "pdd.com" in url:
        return pdd.get_price(url)
    elif "douyin.com" in url or "yinxiang.com" in url:
        return douyin.get_price(url)
    else:
        return {"status": "error", "msg": "不支持的平台"}

if __name__ == "__main__":
    test_url = input("请输入商品链接：")
    result = get_price(test_url)
    print(result)