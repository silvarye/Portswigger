* ✅ : SOLVED (151)
* ❌ : REMAINING (103)

---

* 🟩 : Apprentice (56/56)
* 🟧 : Practitioner (83/162)
* 🟥 : Expert (12/36)

# SQL injection
* 🟩 SQL injection vulnerability in WHERE clause allowing retrieval of hidden data ✅
* 🟩 SQL injection vulnerability allowing login bypass ✅
* 🟧 SQL injection attack, querying the database type and version on Oracle ✅
* 🟧 SQL injection attack, querying the database type and version on MySQL and Microsoft ✅
* 🟧 SQL injection attack, listing the database contents on non-Oracle databases ✅
* 🟧 SQL injection attack, listing the database contents on Oracle ✅
* 🟧 SQL injection UNION attack, determining the number of columns returned by the query ✅
* 🟧 SQL injection UNION attack, finding a column containing text ✅
* 🟧 SQL injection UNION attack, retrieving data from other tables ✅
* 🟧 SQL injection UNION attack, retrieving multiple values in a single column ✅
* 🟧 Blind SQL injection with conditional responses ✅
* 🟧 Blind SQL injection with conditional errors ✅
* 🟧 Visible error-based SQL injection ✅
* 🟧 Blind SQL injection with time delays ✅
* 🟧 Blind SQL injection with time delays and information retrieval ✅
* 🟧 Blind SQL injection with out-of-band interaction ❌
* 🟧 Blind SQL injection with out-of-band data exfiltration ❌
* 🟧 SQL injection with filter bypass via XML encoding ✅

# Cross-site scripting
* 🟩 Reflected XSS into HTML context with nothing encoded ✅
* 🟩 Stored XSS into HTML context with nothing encoded ✅
* 🟩 DOM XSS in document.write sink using source location.search ✅
* 🟩 DOM XSS in innerHTML sink using source location.search ✅
* 🟩 DOM XSS in jQuery anchor href attribute sink using location.search source ✅
* 🟩 DOM XSS in jQuery selector sink using a hashchange event ✅
* 🟩 Reflected XSS into attribute with angle brackets HTML-encoded ✅
* 🟩 Stored XSS into anchor href attribute with double quotes HTML-encoded ✅
* 🟩 Reflected XSS into a JavaScript string with angle brackets HTML encoded ✅
* 🟧 DOM XSS in document.write sink using source location.search inside a select element ✅
* 🟧 DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded ✅
* 🟧 Reflected DOM XSS ✅
* 🟧 Stored DOM XSS ✅
* 🟧 Reflected XSS into HTML context with most tags and attributes blocked ✅
* 🟧 Reflected XSS into HTML context with all tags blocked except custom ones ✅
* 🟧 Reflected XSS with some SVG markup allowed ✅
* 🟧 Reflected XSS in canonical link tag ✅
* 🟧 Reflected XSS into a JavaScript string with single quote and backslash escaped ✅
* 🟧 Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped ✅
* 🟧 Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped ✅
* 🟧 Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped ✅
* 🟧 Exploiting cross-site scripting to steal cookies ✅
* 🟧 Exploiting cross-site scripting to capture passwords ✅
* 🟧 Exploiting XSS to perform CSRF ✅
* 🟥 Reflected XSS with AngularJS sandbox escape without strings ✅
* 🟥 Reflected XSS with AngularJS sandbox escape and CSP ✅
* 🟥 Reflected XSS with event handlers and href attributes blocked ❌
* 🟥 Reflected XSS in a JavaScript URL with some characters blocked ❌
* 🟥 Reflected XSS protected by very strict CSP, with dangling markup attack ❌
* 🟥 Reflected XSS protected by CSP, with CSP bypass ✅

# Cross-site request forgery (CSRF)
* 🟩 CSRF vulnerability with no defenses ✅
* 🟧 CSRF where token validation depends on request method ✅
* 🟧 CSRF where token validation depends on token being present ✅
* 🟧 CSRF where token is not tied to user session ✅
* 🟧 CSRF where token is tied to non-session cookie ✅
* 🟧 CSRF where token is duplicated in cookie ✅
* 🟧 SameSite Lax bypass via method override ❌
* 🟧 SameSite Strict bypass via client-side redirect ✅
* 🟧 SameSite Strict bypass via sibling domain ❌
* 🟧 SameSite Lax bypass via cookie refresh ❌
* 🟧 CSRF where Referer validation depends on header being present ❌
* 🟧 CSRF with broken Referer validation ❌

# Clickjacking
* 🟩 Basic clickjacking with CSRF token protection ✅
* 🟩 Clickjacking with form input data prefilled from a URL parameter ✅
* 🟩 Clickjacking with a frame buster script ✅
* 🟧 Exploiting clickjacking vulnerability to trigger DOM-based XSS ❌
* 🟧 Multistep clickjacking ❌

# DOM-based vulnerabilities
* 🟧 DOM XSS using web messages ❌
* 🟧 DOM XSS using web messages and a JavaScript URL ❌
* 🟧 DOM XSS using web messages and JSON.parse ❌
* 🟧 DOM-based open redirection ❌
* 🟧 DOM-based cookie manipulation ❌
* 🟥 Exploiting DOM clobbering to enable XSS ❌
* 🟥 Clobbering DOM attributes to bypass HTML filters ❌

# Cross-origin resource sharing (CORS)
* 🟩 CORS vulnerability with basic origin reflection ✅
* 🟩 CORS vulnerability with trusted null origin ✅
* 🟧 CORS vulnerability with trusted insecure protocols ❌
* 🟥 CORS vulnerability with internal network pivot attack ❌

# XML external entity (XXE) injection
* 🟩 Exploiting XXE using external entities to retrieve files ✅
* 🟩 Exploiting XXE to perform SSRF attacks ✅
* 🟧 Blind XXE with out-of-band interaction ❌
* 🟧 Blind XXE with out-of-band interaction via XML parameter entities ❌
* 🟧 Exploiting blind XXE to exfiltrate data using a malicious external DTD ✅
* 🟧 Exploiting blind XXE to retrieve data via error messages ✅
* 🟧 Exploiting XInclude to retrieve files ✅
* 🟧 Exploiting XXE via image file upload ✅
* 🟥 Exploiting XXE to retrieve data by repurposing a local DTD ✅

# Server-side request forgery (SSRF)
* 🟩 Basic SSRF against the local server ✅
* 🟩 Basic SSRF against another back-end system ✅
* 🟧 Blind SSRF with out-of-band detection ❌
* 🟧 SSRF with blacklist-based input filter ✅
* 🟧 SSRF with filter bypass via open redirection vulnerability ✅
* 🟥 Blind SSRF with Shellshock exploitation ❌
* 🟥 SSRF with whitelist-based input filter ✅
* 🟥 Blind SSRF with Shellshock exploitation ❌

# HTTP request smuggling
* 🟧 HTTP request smuggling, confirming a CL.TE vulnerability via differential responses ✅
* 🟧 HTTP request smuggling, confirming a TE.CL vulnerability via differential responses ✅
* 🟧 Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability ✅
* 🟧 Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability ✅
* 🟧 Exploiting HTTP request smuggling to reveal front-end request rewriting ✅
* 🟧 Exploiting HTTP request smuggling to capture other users' requests ✅
* 🟧 Exploiting HTTP request smuggling to deliver reflected XSS ✅
* 🟧 Response queue poisoning via H2.TE request smuggling ❌
* 🟧 H2.CL request smuggling ❌
* 🟧 HTTP/2 request smuggling via CRLF injection ❌
* 🟧 HTTP/2 request splitting via CRLF injection ❌
* 🟧 CL.0 request smuggling ❌
* 🟧 HTTP request smuggling, basic CL.TE vulnerability ❌
* 🟧 HTTP request smuggling, basic TE.CL vulnerability ❌
* 🟧 HTTP request smuggling, obfuscating the TE header ❌
* 🟥 Exploiting HTTP request smuggling to perform web cache poisoning ❌
* 🟥 Exploiting HTTP request smuggling to perform web cache deception ❌
* 🟥 Bypassing access controls via HTTP/2 request tunnelling ❌
* 🟥 Web cache poisoning via HTTP/2 request tunnelling ❌
* 🟥 Client-side desync ❌
* 🟥 Browser cache poisoning via client-side desync ❌
* 🟥 Server-side pause-based request smuggling ❌

# OS command injection
* 🟩 OS command injection, simple case ✅
* 🟧 Blind OS command injection with time delays ✅
* 🟧 Blind OS command injection with output redirection ✅
* 🟧 Blind OS command injection with out-of-band interaction ❌
* 🟧 Blind OS command injection with out-of-band data exfiltration ❌

# Server-side template injection
* 🟧 Basic server-side template injection ✅
* 🟧 Basic server-side template injection (code context) ✅
* 🟧 Server-side template injection using documentation ✅
* 🟧 Server-side template injection in an unknown language with a documented exploit ✅
* 🟧 Server-side template injection with information disclosure via user-supplied objects ✅
* 🟥 Server-side template injection in a sandboxed environment ✅
* 🟥 Server-side template injection with a custom exploit ✅

# Directory traversal
* 🟩 File path traversal, simple case ✅
* 🟧 File path traversal, traversal sequences blocked with absolute path bypass ✅
* 🟧 File path traversal, traversal sequences stripped non-recursively ✅
* 🟧 File path traversal, traversal sequences stripped with superfluous URL-decode ✅
* 🟧 File path traversal, validation of start of path ✅
* 🟧 File path traversal, validation of file extension with null byte bypass ✅

# Access control vulnerabilities
* 🟩 Unprotected admin functionality ✅
* 🟩 Unprotected admin functionality with unpredictable URL ✅
* 🟩 User role controlled by request parameter ✅
* 🟩 User role can be modified in user profile ✅
* 🟩 User ID controlled by request parameter ✅
* 🟩 User ID controlled by request parameter, with unpredictable user IDs ✅
* 🟩 User ID controlled by request parameter with data leakage in redirect ✅
* 🟩 User ID controlled by request parameter with password disclosure ✅
* 🟩 Insecure direct object references ✅
* 🟧 URL-based access control can be circumvented ✅
* 🟧 Method-based access control can be circumvented ✅
* 🟧 Multi-step process with no access control on one step ✅
* 🟧 Referer-based access control ✅

# Authentication
* 🟩 Username enumeration via different responses ✅
* 🟩 2FA simple bypass ✅
* 🟩 Password reset broken logic ✅
* 🟧 Username enumeration via subtly different responses ❌
* 🟧 Username enumeration via response timing ❌
* 🟧 Broken brute-force protection, IP block ❌
* 🟧 Username enumeration via account lock ❌
* 🟧 2FA broken logic ✅
* 🟧 Brute-forcing a stay-logged-in cookie ❌
* 🟧 Offline password cracking ❌
* 🟧 Password reset poisoning via middleware ❌
* 🟧 Password brute-force via password change ❌
* 🟥 Broken brute-force protection, multiple credentials per request ❌
* 🟥 2FA bypass using a brute-force attack ❌

# WebSockets
* 🟩 Manipulating WebSocket messages to exploit vulnerabilities ✅
* 🟧 Cross-site WebSocket hijacking ❌
* 🟧 Manipulating the WebSocket handshake to exploit vulnerabilities ❌
* 🟧 Cross-site WebSocket hijacking ❌

# Web cache poisoning
* 🟧 Web cache poisoning with an unkeyed header ✅
* 🟧 Web cache poisoning with an unkeyed cookie ✅
* 🟧 Web cache poisoning with multiple headers ✅
* 🟧 Targeted web cache poisoning using an unknown header ✅
* 🟧 Web cache poisoning via an unkeyed query string ❌
* 🟧 Web cache poisoning via an unkeyed query parameter ❌
* 🟧 Parameter cloaking ❌
* 🟧 Web cache poisoning via a fat GET request ❌
* 🟧 URL normalization ❌
* 🟥 Web cache poisoning to exploit a DOM vulnerability via a cache with strict cacheability criteria ❌
* 🟥 Combining web cache poisoning vulnerabilities ❌
* 🟥 Cache key injection ❌
* 🟥 Internal cache poisoning ❌

# Insecure deserialization
* 🟩 Modifying serialized objects ✅
* 🟧 Modifying serialized data types ❌
* 🟧 Using application functionality to exploit insecure deserialization ❌
* 🟧 Arbitrary object injection in PHP ❌
* 🟧 Exploiting Java deserialization with Apache Commons ❌
* 🟧 Exploiting PHP deserialization with a pre-built gadget chain ❌
* 🟧 Exploiting Ruby deserialization using a documented gadget chain ❌
* 🟥 Developing a custom gadget chain for Java deserialization ❌
* 🟥 Developing a custom gadget chain for PHP deserialization ✅
* 🟥 Using PHAR deserialization to deploy a custom gadget chain ✅

# Information disclosure
* 🟩 Information disclosure in error messages ✅
* 🟩 Information disclosure on debug page ✅
* 🟩 Source code disclosure via backup files ✅
* 🟩 Authentication bypass via information disclosure ✅
* 🟧 Information disclosure in version control history ❌

# Business logic vulnerabilities
* 🟩 Excessive trust in client-side controls ✅
* 🟩 High-level logic vulnerability ✅
* 🟩 Inconsistent security controls ✅
* 🟩 Flawed enforcement of business rules ✅
* 🟧 Low-level logic flaw ✅
* 🟧 Inconsistent handling of exceptional input ✅
* 🟧 Weak isolation on dual-use endpoint ✅
* 🟧 Insufficient workflow validation ❌
* 🟧 Authentication bypass via flawed state machine ❌
* 🟧 Infinite money logic flaw ❌
* 🟧 Authentication bypass via encryption oracle ❌

# HTTP Host header attacks
* 🟩 Basic password reset poisoning ✅
* 🟩 Host header authentication bypass ✅
* 🟧 Web cache poisoning via ambiguous requests ❌
* 🟧 Routing-based SSRF ❌
* 🟧 SSRF via flawed request parsing ❌
* 🟧 Host validation bypass via connection state attack ❌
* 🟥 Password reset poisoning via dangling markup ❌

# OAuth authentication
* 🟩 Authentication bypass via OAuth implicit flow ✅
* 🟧 SSRF via OpenID dynamic client registration ❌
* 🟧 Forced OAuth profile linking ✅
* 🟧 OAuth account hijacking via redirect_uri ✅
* 🟧 Stealing OAuth access tokens via an open redirect ✅
* 🟥 Stealing OAuth access tokens via a proxy page ❌

# File upload vulnerabilities
* 🟩 Remote code execution via web shell upload ✅
* 🟩 Web shell upload via Content-Type restriction bypass ✅
* 🟧 Web shell upload via path traversal ✅
* 🟧 Web shell upload via extension blacklist bypass ✅
* 🟧 Web shell upload via obfuscated file extension ✅
* 🟧 Remote code execution via polyglot web shell upload ✅
* 🟥 Web shell upload via race condition ✅

# JWT
* 🟩 JWT authentication bypass via unverified signature ✅
* 🟩 JWT authentication bypass via flawed signature verification ✅
* 🟧 JWT authentication bypass via weak signing key ✅
* 🟧 JWT authentication bypass via jwk header injection ✅
* 🟧 JWT authentication bypass via jku header injection ✅
* 🟧 JWT authentication bypass via kid header path traversal ✅
* 🟥 JWT authentication bypass via algorithm confusion ✅
* 🟥 JWT authentication bypass via algorithm confusion with no exposed key ✅

# Essential skills
* 🟧 Discovering vulnerabilities quickly with targeted scanning ❌

# Prototype pollution
* 🟧 Client-side prototype pollution via browser APIs ❌
* 🟧 DOM XSS via client-side prototype pollution ❌
* 🟧 DOM XSS via an alternative prototype pollution vector ❌
* 🟧 Client-side prototype pollution via flawed sanitization ❌
* 🟧 Client-side prototype pollution in third-party libraries ❌
* 🟧 Privilege escalation via server-side prototype pollution ❌
* 🟧 Detecting server-side prototype pollution without polluted property reflection ❌
* 🟧 Bypassing flawed input filters for server-side prototype pollution ❌
* 🟧 Remote code execution via server-side prototype pollution ❌
* 🟥 Exfiltrating sensitive data via server-side prototype pollution ❌

# GraphQL API vulnerabilities
* 🟩 Accessing private GraphQL posts ✅
* 🟧 Accidental exposure of private GraphQL fields ❌
* 🟧 Finding a hidden GraphQL endpoint ❌
* 🟧 Bypassing GraphQL brute force protections ❌
* 🟧 Performing CSRF exploits over GraphQL ❌

# Race conditions
* 🟩 Limit overrun race conditions ✅
* 🟧 Bypassing rate limits via race conditions ❌
* 🟧 Multi-endpoint race conditions ❌
* 🟧 Single-endpoint race conditions ❌
* 🟧 Exploiting time-sensitive vulnerabilities ❌
* 🟥 Partial construction race conditions ❌

# NoSQL injection
* 🟩 Detecting NoSQL injection ✅
* 🟩 Exploiting NoSQL operator injection to bypass authentication ✅
* 🟧 Exploiting NoSQL injection to extract data ❌
* 🟧 Exploiting NoSQL operator injection to extract unknown fields ❌

