# Tests SSL 

* testssl.sh
```
./testssl.sh -oA output_file target_url
```
* https://www.ssllabs.com/ssltest/

# Subdomain
* https://subdomainfinder.c99.nl/
* Amass
```
amass enum -d DOMAIN_NAME
```
* https://github.com/michenriksen/aquatone

# Port scan

Fast nmap :
```
nmap -F -vvv -Pn -sT --open --reason --max-rate 50 -sV -oA output_file -iL list_of_target
```

# Fuzzing

* Ffuf
```
ffuf -r -c -H "User-Agent: Bugbounty" -of html -fs $size -t 4 -sa -p 0.08 -mc all -w $wordlist -c -u https://targeted_website/FUZZ -o ./output_file
```

# Discovery 
* https://www.shodan.io/
* Censys
* https://archive.org/web/
