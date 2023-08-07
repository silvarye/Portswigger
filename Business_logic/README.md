```
Lab: Excessive trust in client-side controls

APPRENTICE

This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

You can log in to your own account using the following credentials: wiener:peter 
```
Intercept when you add the product in your basket, then change the price <3

---

```
Lab: High-level logic vulnerability

APPRENTICE

This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

You can log in to your own account using the following credentials: wiener:peter 
```
1. Intercept when you add the product in your basket
2. Change the quantity to a negative value
3. Use other product for decrease the Jacket's price with negative quantity

---

```
Lab: Inconsistent security controls

APPRENTICE

This lab's flawed logic allows arbitrary users to access administrative functionality that should only be available to company employees. To solve the lab, access the admin panel and delete the user carlos. 
```
1. Intercept when you register yourself for changing the email and bypass client securty restriction
2. Then on your account menu changing your mail in anything@dontwannacry.net
3. Go to /admin and remove that moron Carlos

---
```
Lab: Flawed enforcement of business rules

APPRENTICE

This lab has a logic flaw in its purchasing workflow. To solve the lab, exploit this flaw to buy a "Lightweight l33t leather jacket".

You can log in to your own account using the following credentials: wiener:peter 
```

1. Sign up to the newsletter
2. Get new coupon reduction
3. Alternate between NEWCUST5 / SIGNUP30 up to 0$

---

```
Lab: Low-level logic flaw

PRACTITIONER

This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

You can log in to your own account using the following credentials: wiener:peter 
```

1. Use business_logic.py
2. Use a calculator to know the qty needed to overflow (max int 2147483647)
3. Go up to have a price under 100$

---

```
Lab: Inconsistent handling of exceptional input

PRACTITIONER

This lab doesn't adequately validate user input. You can exploit a logic flaw in its account registration process to gain access to administrative functionality. To solve the lab, access the admin panel and delete the user carlos. 
```

1. Use this mail for register : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab@dontwannacry.com.exploit-0a4900d30424f3a282ca06fe014c0016.exploit-server.net
2. The server just take 255 first char so he stop after ".com"
3. Login with you login/password
4. delete user carlos

---

