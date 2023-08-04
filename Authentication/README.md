```
Lab: Username enumeration via different responses

APPRENTICE

This lab is vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

    Candidate usernames
    Candidate passwords

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 
```
archie:hockey

---

```
Lab: Password reset broken logic

APPRENTICE

This lab's password reset functionality is vulnerable. To solve the lab, reset Carlos's password then log in and access his "My account" page.

    Your credentials: wiener:peter
    Victim's username: carlos

```
forgot password -> username= ~wiener~ carlos&new-password-1=test&new-password-2=test

---

```
This lab's two-factor authentication is vulnerable due to its flawed logic. To solve the lab, access Carlos's account page.

Your credentials: wiener:peter
Victim's username: carlos

You also have access to the email server to receive your 2FA verification code. 
```

GET /login2

Cookie: session=O6oKDwmJprafDoewXUsAz5SzLKxnLvJ7; verify=wiener

Change the `verify` cookie param from `wiener` to `carlos`. The request for carlos 2FA was made so just trying to BF the MFA ?

```
POST /login2 
mfa-code=XXXX 
```

Run the python script with the arg `-w four_digit_mfa_wordlist.txt`

> Congratulations, you solved the lab!


---

```
This lab's two-factor authentication is vulnerable to brute-forcing. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, brute-force the 2FA code and access Carlos's account page.

Victim's credentials: carlos:montoya 
```

The code uses the Pool class from multiprocessing to distribute the processing of mfa-codes across multiple processes. The number of processes created is equal to the number of CPU cores on the machine, which is obtained using the cpu_count() function. Each mfa-code is processed by the process_mfa_code function, which is run in a separate process. The results of each process are collected in the results list, which is then checked for successful mfa-codes.

---

```
This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, access Carlos's account page.

Your credentials: wiener:peter
Victim's credentials carlos:montoya
```

Just access Carlos's account page with his creds without validate the 2FA.

> Congratulations, you solved the lab!

---

```
This lab uses an OAuth service to allow users to log in with their social media account. Flawed validation by the client application makes it possible for an attacker to log in to other users' accounts without knowing their password.

To solve the lab, log in to Carlos's account. His email address is carlos@carlos-montoya.net.

You can log in with your own social media account using the following credentials: wiener:peter. 
```

Lors de l'appel à : `/authenticate``

- Changer l'adresse email de Peter par cette de Carlos

> SOLVED GOOD JOB ! :)

---


---



---



---



---



