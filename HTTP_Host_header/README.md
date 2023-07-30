```
Lab: Basic password reset poisoning

APPRENTICE

This lab is vulnerable to password reset poisoning. The user carlos will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account.

You can log in to your own account using the following credentials: wiener:peter. Any emails sent to this account can be read via the email client on the exploit server. 
```

1. Change Host header to you exploit server id when you ask for reset your password
2. Change the username who asking this ~wiener~ carlos
3. See the log of the exploit server
4. Use this token for reset Carlos's pswd

---

```
Lab: Host header authentication bypass

APPRENTICE

This lab makes an assumption about the privilege level of the user based on the HTTP Host header.

To solve the lab, access the admin panel and delete the user carlos. 
```

GET /admin/delete?username=carlos HTTP/2
Host: localhost

---