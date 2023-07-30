# Recap

| 1 | 2 | 3 | 4 |   5     |
|-------|-------|----------|-------|----------------|
| SQLI  | XSS   |  XSS     | JWT   |XXE + SSRF + OS_CMD_INJECTION|

 | 6 | 7 | 8 |   9     |
|-------|----------|-------|----------------|
| CSRF + CORS + Clickjacking  |   SSTI + Information_disclosure    | HTTP_request_smuggling + Access_control   |  Finish all the resting Apprentice labs |


## 1 : 


* SQL injection vulnerability in WHERE clause allowing retrieval of hidden data (APPRENTICE) ✅
* SQL injection vulnerability allowing login bypass (APPRENTICE) ✅
* SQL injection attack, querying the database type and version on Oracle (PRACTITIONER) ✅
* SQL injection attack, querying the database type and version on MySQL and Microsoft (PRACTITIONER) ✅
* SQL injection attack, listing the database contents on non-Oracle databases ✅
* SQL injection attack, listing the database contents on Oracle (PRACTITIONER) ✅ 
* SQL injection UNION attack, determining the number of columns returned by the query (PRACTITIONER) ✅
* SQL injection UNION attack, finding a column containing text (PRACTITIONER) ✅
* SQL injection UNION attack, retrieving data from other tables (PRACTITIONER) ✅
* SQL injection UNION attack, retrieving multiple values in a single column (PRACTITIONER) ✅
* Blind SQL injection with conditional responses (PRACTITIONER) ✅
* Blind SQL injection with conditional errors (PRACTITIONER) ✅
* Blind SQL injection with time delays (PRACTITIONER) ✅
* Blind SQL injection with time delays and information retrieval (PRACTITIONER) ✅
* SQL injection with filter bypass via XML encoding (PRACTITIONER) ✅

## 2 : 

* Reflected XSS into HTML context with nothing encoded (APPRENTICE) ✅
* Stored XSS into HTML context with nothing encoded (APPRENTICE) ✅
* DOM XSS in document.write sink using source location.search (APPRENTICE) ✅
* DOM XSS in innerHTML sink using source location.search (APPRENTICE) ✅
* DOM XSS in jQuery anchor href attribute sink using location.search source (APPRENTICE) ✅
* DOM XSS in jQuery selector sink using a hashchange event (APPRENTICE) ✅
* Reflected XSS into attribute with angle brackets HTML-encoded (APPRENTICE) ✅
* Stored XSS into anchor href attribute with double quotes HTML-encoded (APPRENTICE) ✅
* Stored XSS into anchor href attribute with double quotes HTML-encoded (APPRENTICE) ✅
* DOM XSS in document.write sink using source location.search inside a select element (PRACTITIONER) ✅
* DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded (PRACTITIONER) ✅
* Reflected DOM XSS (PRACTITIONER) ✅
* Stored DOM XSS (PRACTITIONER) ✅
* Reflected XSS into HTML context with most tags and attributes blocked (PRACTITIONER) ✅
* Reflected XSS into HTML context with all tags blocked except custom ones (PRACTITIONER) ✅
* Reflected XSS with some SVG markup allowed (PRACTITIONER) ✅

## 3 :

* Reflected XSS in canonical link tag (PRACTITIONER) ✅
* Reflected XSS into a JavaScript string with single quote and backslash escaped (PRACTITIONER) ✅
* Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped (PRACTITIONER) ✅
* Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped (PRACTITIONER) ✅
* Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped (PRACTITIONER) ✅
* Exploiting cross-site scripting to steal cookies (PRACTITIONER) ✅
* Exploiting cross-site scripting to capture passwords (PRACTITIONER) ✅
* Exploiting XSS to perform CSRF (PRACTITIONER) ✅
* Reflected XSS with AngularJS sandbox escape without strings (EXPERT) ✅
* Reflected XSS with AngularJS sandbox escape and CSP (EXPERT) ✅
* Reflected XSS with event handlers and href attributes blocked (EXPERT) ✅
* Reflected XSS protected by CSP, with CSP bypass (EXPERT) ✅

## 4 :

* JWT authentication bypass via unverified signature (APPRENTICE) ✅
* JWT authentication bypass via flawed signature verification (APPRENTICE) ✅
* JWT authentication bypass via weak signing key (PRACTITIONER) ✅
* JWT authentication bypass via jwk header injection (PRACTITIONER) ✅
* JWT authentication bypass via jku header injection (PRACTITIONER) ✅
* JWT authentication bypass via kid header path traversal (PRACTITIONER) ✅
* JWT authentication bypass via algorithm confusion with no exposed key (EXPERT) ✅

## 5 :

* Exploiting XXE using external entities to retrieve files (APPRENTICE) ✅
* Exploiting XXE to perform SSRF attacks (APPRENTICE) ✅
* Exploiting blind XXE to exfiltrate data using a malicious external DTD (PRACTITIONER) ✅
* Exploiting blind XXE to retrieve data via error messages (PRACTITIONER) ✅
* Exploiting XInclude to retrieve files (PRACTITIONER) ✅
* Exploiting XXE via image file upload (PRACTITIONER) ✅
* Basic SSRF against the local server (APPRENTICE) ✅
* Basic SSRF against another back-end system (APPRENTICE) ✅
* SSRF with blacklist-based input filter (PRACTITIONER) ✅
* SSRF with filter bypass via open redirection vulnerability (PRACTITIONER) ✅
* SSRF with whitelist-based input filter (EXPERT) ✅
* OS command injection, simple case (APPRENTICE) ✅
* Blind OS command injection with time delays (PRACTITIONER) ✅
* Blind OS command injection with output redirection (PRACTITIONER) ✅
* Blind OS command injection with output redirection (PRACTITIONER) ✅

---

## 6 : 

* CSRF vulnerability with no defenses (APPRENTICE) ✅
* CSRF where token validation depends on request method (PRACTITIONER) ✅
* CSRF where token validation depends on token being present (PRACTITIONER) ✅
* CSRF where token is not tied to user session (PRACTITIONER) ✅
* CSRF where token is tied to non-session cookie (PRACTITIONER) ✅
* CSRF where token is duplicated in cookie (PRACTITIONER) ✅
* SameSite Strict bypass via client-side redirect (PRACTITIONER) ✅
* CORS vulnerability with basic origin reflection (APPRENTICE) ✅
* Basic clickjacking with CSRF token protection (APPRENTICE) ✅


## 7 :

* Basic server-side template injection (PRACTITIONER) ✅
* Basic server-side template injection (code context) (PRACTITIONER) ✅
* Server-side template injection using documentation (PRACTITIONER) ✅
* Server-side template injection in an unknown language with a documented exploit (PRACTITIONER) ✅
* Server-side template injection with information disclosure via user-supplied objects (PRACTITIONER) ✅
* Server-side template injection with a custom exploit (EXPERT) ✅
* Server-side template injection in a sandboxed environment (EXPERT) ✅
* Information disclosure in error messages (APPRENTICE) ✅
* Information disclosure on debug page (APPRENTICE) ✅
* Source code disclosure via backup files (APPRENTICE) ✅
* Authentication bypass via information disclosure (APPRENTICE) ✅


## 8 :

* HTTP request smuggling, confirming a CL.TE vulnerability via differential responses (PRACTITIONER) ✅
* HTTP request smuggling, confirming a TE.CL vulnerability via differential responses (PRACTITIONER) ✅
* Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability (PRACTITIONER) ✅
* Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability (PRACTITIONER) ✅
* Exploiting HTTP request smuggling to reveal front-end request rewriting (PRACTITIONER) ✅
* Exploiting HTTP request smuggling to capture other users' requests (PRACTITIONER) ✅
* Exploiting HTTP request smuggling to deliver reflected XSS (PRACTITIONER) ✅
* User ID controlled by request parameter with data leakage in redirect (APPRENTICE) ✅
* User ID controlled by request parameter with password disclosure (APPRENTICE) ✅
* Insecure direct object references (APPRENTICE) ✅

## 9 :

* Basic clickjacking with CSRF token protection (APPRENTICE) ✅
* Clickjacking with a frame buster script (APPRENTICE) ✅
* CORS vulnerability with trusted null origin (APPRENTICE) ✅
* File path traversal, simple case (APPRENTICE) ✅
* Username enumeration via different responses (APPRENTICE) ✅
* Password reset broken logic (APPRENTICE) ✅
* Manipulating WebSocket messages to exploit vulnerabilities (APPRENTICE) ✅
* Modifying serialized objects (APPRENTICE) ✅
* Excessive trust in client-side controls (APPRENTICE) ✅
* High-level logic vulnerability (APPRENTICE) ✅
* Inconsistent security controls (APPRENTICE) ✅
* Flawed enforcement of business rules (APPRENTICE) ✅
* Basic password reset poisoning (APPRENTICE) ✅
* Host header authentication bypass (APPRENTICE) ✅
* Accessing private GraphQL posts (APPRENTICE) ✅
* Remote code execution via web shell upload (APPRENTICE) ✅
* Host header authentication bypass (APPRENTICE) ✅
