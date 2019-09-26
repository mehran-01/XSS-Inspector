import requests
from bs4 import BeautifulSoup
# import mechanize
# import urllib.request  as urllib2 
# import re
# import html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException

url_base = "http://172.20.9.225"
#------------------------------------#
#info to create a new users
login = "bee"
password = "bug"
email = "beez@site.com"

#add a session to the request
s = requests.session()
#create a header to add it to the request
headers = {
	'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
}


#------------------------------------#
#user login page with passed info
url_login = url_base + "/bWAPP/login.php"

request = s.get(url_login)

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

print(inputFieldNames)


browser = webdriver.Firefox()
browser.get(url_login) 
# time.sleep(10)


username = browser.find_element_by_xpath("""//*[@id="login"]""")
password = browser.find_element_by_xpath("""//*[@id="password"]""")

username.send_keys("bee")
password.send_keys("bug")

login_attempt = browser.find_element_by_name("form")
login_attempt.submit()
