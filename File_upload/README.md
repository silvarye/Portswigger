```
Lab: Remote code execution via web shell upload

APPRENTICE

This lab contains a vulnerable image upload function. It doesn't perform any validation on the files users upload before storing them on the server's filesystem.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter 
```

1. Upload webshell.php
2. cat /home/carlos/secret

---

```
Lab: Host header authentication bypass

APPRENTICE

This lab makes an assumption about the privilege level of the user based on the HTTP Host header.

To solve the lab, access the admin panel and delete the user carlos. 
```

1. Upload webshell.php
2. Change content-type to image/jpeg
3. cat /home/carlos/secret

---

```
Lab: Web shell upload via path traversal

PRACTITIONER

This lab contains a vulnerable image upload function. The server is configured to prevent execution of user-supplied files, but this restriction can be bypassed by exploiting a secondary vulnerability.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter 
```

1. Upload webshell.php
2. Look that there are no restriction on the upload file functionnality but the php is not interpreted on the location where the file is uploaded
3. Change the filename to perform path traversal in order to uplaod the file where the php can be interpreted
4. filename="..%2Fwebshell.php"
5. Go to files/webshell.php
6. enjoy your RCE
7. cat /home/carlos/secret


---

```
Lab: Web shell upload via extension blacklist bypass

PRACTITIONER

This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed due to a fundamental flaw in the configuration of this blacklist.

To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter 
```

1. Upload webshell.php
2. Bypass restriciton with .php5
3. Add this extension via .htaccess as executable :
```
filename=".htaccess"
Content-Type : text/plain
AddType application/x-httpd-php .php5
```
4. Reload your webshell and now it's interpreted
5. cat /home/carlos/secret

---

```
Lab: Web shell upload via obfuscated file extension

PRACTITIONER
LAB Not solved

This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed using a classic obfuscation technique.

To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter 
```

1. Upload webshell.php
2. See that only JPEG and PNG are allowed
3. Bypass extension verification with : .php%00.png


---

```
Lab: Remote code execution via polyglot web shell upload

PRACTITIONER

This lab contains a vulnerable image upload function. Although it checks the contents of the file to verify that it is a genuine image, it is still possible to upload and execute server-side code.

To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: wiener:peter 
```

1. Upload webshell.php

---
