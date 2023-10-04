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