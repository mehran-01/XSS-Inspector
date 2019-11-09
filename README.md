### XSS Inspector is an automated penetration testing tool to find XSS vulnerabilities on web applications
* Note: this app built for vulnerabilities testing purposes by an authorized user so use it at your own responsibility


### Difference with similar tools
* Open Source
* Python 3 
* Read from infinite payloads automatically
* Login to any website automatically(worked on most cases)
* See injections in real time in browser
* Get report of the result stored as a CSV
* More features will be added ...

### Requirements:
Install Python3

Install packages:
>pip install requests bs4 selenium argparse

Download geckodriver Firefox from:
https://github.com/mozilla/geckodriver/releases

Add driver to your PATH(e.g. in linux):
>export PATH="/path/to/dir:$PATH"

### XSS Inspector:
**Help:**
>python auto.py -h

![Alt text](/images/XSS-Inspector-help-command.png?raw=true "help command")

**Test on a XSS *vulnerable website* (e.g. Google Gruyere):**
* Note: id in url is the instance that I've created but you can create yours through https://google-gruyere.appspot.com/start

>python auto.py -h https://google-gruyere.appspot.com/618655413586375839657115594994104056558/

![Alt text](/images/XSS-Inspector-Google-Gruyere-terminal.png?raw=true "Google Gruyere terminal")

*Started injecting payloads immediately and some of payloads were injected and means it's vulnerable to those payloads*

![Alt text](/images/XSS-Inspector-Google-Gruyere-Firefox.png?raw=true "auto XSSer Google Gruyere Firefox")

**Test on a *non XSS vulnerable website*, possibly! (e.g. errorhandle.com my own website!)**
>python auto.py -h https://errorhandle.com

![Alt text](/images/XSS-Inspector-eH-Firefox.png?raw=true "auto XSSer errorHandle Firefox")

*Not logged in but started injecting payloads immediately but payloads were not injected sicne it's not vulnerable, possibly! *

**(Optional) Pass user and password to login to the website automatically (e.g. errorhandle.com my own website!) :**
>python auto.py -h https://errorhandle.com -user [your username] -password [your password]

![Alt text](/images/XSS-Inspector-eH-loggedin-Firefox.png?raw=true "auto XSSer errorHandle logged in Firefox")

*Logged in automatically and started injecting payloads but payloads were not injected since it's not vulnerable, possibly! *
