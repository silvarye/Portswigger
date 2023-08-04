import subprocess

php_ini_path = "../tools/php.ini"
php_script_path = "../tools/phar_jpg_polyglot.php"
command = ["sudo", "php", "-c", php_ini_path, php_script_path]
subprocess.run(command)
