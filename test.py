import requests

#------------------------------------#
#info to create a new users
login = "bee"
password = "bug"
email = "beez@site.com"
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
createUserResponse


