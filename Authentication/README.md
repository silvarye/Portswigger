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
