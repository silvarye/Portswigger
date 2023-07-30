```
Lab: CSRF vulnerability with no defenses

APPRENTICE

This lab's email change functionality is vulnerable to CSRF.

To solve the lab, craft some HTML that uses a CSRF attack to change the viewer's email address and upload it to your exploit server.

You can log in to your own account using the following credentials: wiener:peter 
```
> csrfPoc1.html

---
```
Lab: CSRF where token validation depends on request method

PRACTITIONER

This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies defenses to certain types of requests.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: wiener:peter 
```
> csrfPoc2.html

---
```
Lab: CSRF where token validation depends on token being present

PRACTITIONER

This lab's email change functionality is vulnerable to CSRF.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: wiener:peter 
```
> csrfPoc3.html

---
```
Lab: CSRF where token is not tied to user session

PRACTITIONER

This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't integrated into the site's session handling system.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You have two accounts on the application that you can use to help design your attack. The credentials are as follows:

    wiener:peter
    carlos:montoya

```
Use your csrf token to lauch the attack, you should see that the csrf token is not tied to user session

> csrfPoc4.html

---

```
Lab: CSRF where token is tied to non-session cookie

PRACTITIONER

This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't fully integrated into the site's session handling system.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You have two accounts on the application that you can use to help design your attack. The credentials are as follows:

    wiener:peter
    carlos:montoya


```

> csrfPoc5.html

---
```
Lab: CSRF where token is duplicated in cookie

PRACTITIONER

This lab's email change functionality is vulnerable to CSRF. It attempts to use the insecure "double submit" CSRF prevention technique.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: wiener:peter 
```

> csrfPoc6.html

---
```
Lab: SameSite Strict bypass via client-side redirect

PRACTITIONER

This lab's change email function is vulnerable to CSRF. To solve the lab, perform a CSRF attack that changes the victim's email address. You should use the provided exploit server to host your attack.

You can log in to your own account using the following credentials: wiener:peter 
```

> csrfPoc7.html

---