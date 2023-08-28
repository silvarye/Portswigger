## Attaque par Fusion Classique-Fédérée

1. L'attaquant crée un compte sur un site vulnérable avec son adresse mail.
2. L'attaquant change l'adresse mail lié à son compte pour celle de la victime.
3. La victime se connecte avec une identité féderée.
4. L'attaquant peut alors accèder au compte de la victime.

## Attaque par Identifiant de Session Non Expiré

1. L'attaquant crée un compte sur un site vulnérable avec l'adresse mail de la victime et maintient une session active de longue durée (reste connecté).
2. La victime crée son compte mais le compte existe déjà. Il aura donc la possibilité de réinitialiser son mot de passe.
3. La session de l'attaquant étant toujours en cours il pourra alors accèder au compte de la victime.

## Attaque Trojan

1. L'attaquant crée un compte sur un site vulnérable avec l'adresse mail de la victime.
2. L'attaquant met en place une option de récupération de compte avec son email ou un compte de réseau social qu'il maitrise.
3. La victime crée son compte mais le compte existe déjà. Il aura donc la possibilité de réinitialiser son mot de passe.
4. L'attaquant ainsi que la victime reçevront tout deux la notification pour changer le mot de passe et l'attaquant pourra alors utiliser ce lien pour changer le mot de passe de la victime et ainsi voler les informations de la victime.

## Attaque de Changement d'Adresse E-mail Non Expirée

1. L'attaquant crée un compte sur un site vulnérable avec l'adresse mail de la victime.
2. L'attaquant fait une demande de changement de mail avec une adresse mail qu'il maîtrise mais ne clique pas sur le lien de validation.
3. La victime crée son compte mais le compte existe déjà. Il aura donc la possibilité de réinitialiser son mot de passe.
4. L'attaquant utilise le lien de changement de mail afin d'acceder au compte de la victime.

## Utilisation non sécurisée de l'idp 

1. L'attaquant utilise un IdP qui ne vérifie pas la propriété d'une adresse électronique lors de la création d'une identité fédérée
2. L'attaquant crée un compte sur un site vulnérable. 
3. La victime crée un compte en utilisant la voie "classique"
4. Le service fusionne incorrectement les deux comptes sur la base de l'adresse électronique
5. L'attaquant peut accéder au compte de la victime.