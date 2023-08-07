import requests
import re

def send_post_request():
    post_data = {
        "productId": "1",
        "redir": "PRODUCT",
        "quantity": "21"
    }

    headers = {
        "Host": "0ac900b803547f37807cd508007300d1.web-security-academy.net",
        "Cookie": "session=JhtELYAB9AlioI4UWIF2XT9qCKTWEkGi",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "37",
        "Origin": "https://0ac900b803547f37807cd508007300d1.web-security-academy.net",
        "Referer": "https://0ac900b803547f37807cd508007300d1.web-security-academy.net/product?productId=1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "X-Pwnfox-Color": "green",
        "Te": "trailers"
    }

    post_url = "https://0ac900b803547f37807cd508007300d1.web-security-academy.net/cart"

    requests.post(post_url, headers=headers, data=post_data)
    #for i in range(320):
    #    requests.post(post_url, headers=headers, data=post_data)
    

if __name__ == "__main__":
    
    send_post_request()



