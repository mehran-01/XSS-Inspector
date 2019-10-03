### auto-XSSer is An an automated penetration testing tool to test XSS vulnerabilities on web applications
* Note:* this app built for velnerabalities testing purporse by an authorised user so I m not responsible for any misuse

### Requirements:
Download geckodriver from for Firefox from link below:
https://github.com/mozilla/geckodriver/releases

Run:
>pip install -r requirements.txt


Add driver to your PATH(e.g. in linux):
>export PATH="/path/to/dir:$PATH"

### auto-XSSer:
**Help:**
>python auto.py -h

usage: auto.py [-h] -url URL [-login LOGIN] [-user USER] [-password PASSWORD]

Pass arguments if necessary

optional arguments:
  -h, --help          show this help message and exit
  -login LOGIN        login url if you want to login and it's not target
                      url/login
  -user USER          username if you want to login
  -password PASSWORD  password if you want to login

required argument(s):
  -url URL            target url



**Run on Google Gruyere(a XSS *vulnerable website*):**
* Note: id in url is the instance I created but you can create your in https://google-gruyere.appspot.com/start *
>python auto.py -h https://google-gruyere.appspot.com/618655413586375839657115594994104056558/



**Run on *non vulnerable website*(e.g. facebook.com at your own risk)**
python auto.py -h https://facebook.com


**Pass user and password to login to the website automatically(e.g. facebook.com at your own risk) :**
>python auto.py -h https://facebook.com -user your user name -password your password