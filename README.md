### XSS Inspector is an automated penetration testing tool to find XSS vulnerabilities on web applications
* Note: this app built for vulnerabilities testing purposes by an authorized user so use it at your own responsibility


### Difference with similar tools
* Python 3 
* Read from infinite payloads automatically
* Handling alerts to click automatically
* Login to any website automatically(worked on most cases)
* See injections in real time in browser
* Get report of the result stored as a CSV
* More features will be added ...

### Requirements:
1) Install Python3

2) Install packages:
>pip install requests bs4 selenium argparse

3) Download geckodriver Firefox from:
https://github.com/mozilla/geckodriver/releases

4) Add driver to your PATH(e.g. in linux):
>export PATH="/path/to/dir:$PATH"

### XSS Inspector:
**Help:**
>python auto.py -h

![Alt text](/images/XSS-Inspector-help-command.png?raw=true "help command")

**Test on a XSS *vulnerable website* (e.g. Google Gruyere):**
* Note: id in url is the instance that I've created but you can create yours through https://google-gruyere.appspot.com/start

>python auto.py -url https://google-gruyere.appspot.com/618655413586375839657115594994104056558/

![Alt text](/images/XSS-Inspector-Google-Gruyere-terminal.png?raw=true "Google Gruyere terminal")

*Started injecting payloads immediately and some of payloads were injected and means it's vulnerable to those payloads*

![Alt text](/images/XSS-Inspector-Google-Gruyere-Firefox.png?raw=true "auto XSSer Google Gruyere Firefox")

**Test on a *non XSS vulnerable website*. (e.g. errorhandle.com my own website!)**
>python auto.py -url https://errorhandle.com

![Alt text](/images/XSS-Inspector-eH-terminal.png?raw=true "eH terminal")

*Started injecting payloads immediately and none of payloads were injected and means it's not vulnerable to those payloads*

![Alt text](/images/XSS-Inspector-eH-Firefox.png?raw=true "auto XSSer errorHandle Firefox")

* Not logged in and started injecting payloads immediately but payloads were not injected sicne suppose to not be vulnerable.

**(Optional) Pass user and password to login to the website automatically (e.g. errorhandle.com my own website!) :**
>python auto.py -url https://errorhandle.com -user [your username] -password [your password]

![Alt text](/images/XSS-Inspector-eH-loggedin-Firefox.png?raw=true "auto XSSer errorHandle logged in Firefox")

* Logged in automatically and started injecting payloads but payloads were not injected since it's not vulnerable, possibly!

* Finally you can get a CSV report of injected payloads in output folder(there won't be any report in output folder if non of payloads were injected)
