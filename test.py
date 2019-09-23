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

