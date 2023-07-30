```
Lab: Information disclosure in error messages

APPRENTICE

This lab's verbose error messages reveal that it is using a vulnerable version of a third-party framework. To solve the lab, obtain and submit the version number of this framework. 
```
> productId=test

Stack trace : 
Apache Struts 2 2.3.31

---

```
Lab: Information disclosure on debug page

APPRENTICE

This lab contains a debug page that discloses sensitive information about the application. To solve the lab, obtain and submit the SECRET_KEY environment variable. 
```

dirb URL

Found cgi-bin > dirlisting on this endpoint 
phpinfo.php > SECRET_KEY 

---


```
Lab: Source code disclosure via backup files

APPRENTICE

This lab leaks its source code via backup files in a hidden directory. To solve the lab, identify and submit the database password, which is hard-coded in the leaked source code. 
```

dirb URL

Found /backup

---


```
Lab: Authentication bypass via information disclosure

APPRENTICE

This lab's administration interface has an authentication bypass vulnerability, but it is impractical to exploit without knowledge of a custom HTTP header used by the front-end.

To solve the lab, obtain the header name then use it to bypass the lab's authentication. Access the admin interface and delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter  
```

dirb URL

Found /admin

 Admin interface only available to local users 

By reading Portswigger course :

`the HTTP TRACE method is designed for diagnostic purposes`

Change the methode to TRACE

> X-Custom-IP-Authorization: 81.80.49.11

Use this instead when you go to /admin
> X-Custom-Ip-Authorization: 127.0.0.1

Then :

> /admin/delete?username=carlos 

GG 

---
