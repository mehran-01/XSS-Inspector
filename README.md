### auto-XSSer is An an automated penetration testing tool to test XSS vulnerabilities on web applications
* Note: this app built for vulnerabilities testing purporses by an authorised user so use it at your own responsibility

### Requirements:
Install Python:
https://realpython.com/installing-python/

Install packages:
>pip install requests bs4 selenium argparse

Download geckodriver Firefox from:
https://github.com/mozilla/geckodriver/releases

Add driver to your PATH(e.g. in linux):
>export PATH="/path/to/dir:$PATH"

### auto-XSSer:
**Help:**
>python auto.py -h

![Alt text](/images/auto-XSSer-help-command.png?raw=true "help command")

**Test on a XSS *vulnerable website* (e.g. Google Gruyere):**
* Note: id in url is the instance that I've created but you can create yours through https://google-gruyere.appspot.com/start

>python auto.py -h https://google-gruyere.appspot.com/618655413586375839657115594994104056558/

![Alt text](/images/auto-XSSer-Google-Gruyere-terminal.png?raw=true "Google Gruyere terminal")

**Started injecting payloads immediately and some of payloads were injected**

![Alt text](/images/auto-XSSer-Google-Gruyere-Firefox.png?raw=true "auto XSSer Google Gruyere Firefox")

**Test on a *non XSS vulnerable website*, possibly! (e.g. facebook.com at your own responsibility!)**
>python auto.py -h https://facebook.com

![Alt text](/images/auto-XSSer-Facebook-Firefox.png?raw=true "auto XSSer Facebook Firefox")

**Not logged in but started injecting payloads immediately**

**(Optional) Pass user and password to login to the website automatically(e.g. facebook.com at your own responsibility) :**
>python auto.py -h https://facebook.com -user [your user name] -password [your password]

![Alt text](/images/auto-XSSer-Facebook-loggedin-Firefox.png?raw=true "auto XSSer Facebook logged in Firefox")

**Logged in automaticaly and started injecting payloads**