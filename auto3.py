import requests
from bs4 import BeautifulSoup
import time
import argparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




browser = webdriver.Firefox()



#get all input fields to find crdentials login fields
def getAllInputFields(url):
	url_login = url + "/login"
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
def findLoginFieldsAndLogin(browser,inputFieldNames, inputFieldLabels, url, user, password): 
	#user login page with passed info
	url_login = url + "/login"
	#browse login url
	browser.get(url_login) 
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
		try:
			login_attempt = browser.find_element_by_xpath("""//button[@type='submit']""")
			print("submit button clicked")
			login_attempt.submit()
			print("logged in")
		except:
			print("didn't login")



#handle if alert pops up to be able to go to the next script
def handleAlert(browser, url, payload, sleep_time):
  newurl = str(url)+"/"+str(payload)
  browser.get(newurl);
  try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert popped up and accepted")
    time.sleep(sleep_time)
  except:
    print("no alert popped up")
    time.sleep(sleep_time)
  finally:
  	current_url = browser.current_url
  	r = requests.get(current_url)
  	if payload.rstrip('\n') in r.content:
  		print("was able to inject: " + payload)
  	else:
  		print("was not injected!")
  time.sleep(sleep_time)



#injecting top500 xss scripts to the target
def injectPayload(payloads, url):
	with open(payloads, "r") as pl:
		print("started injecting payloads")
	  	for payload in pl:
	  		handleAlert(browser, url, payload, 1)






parser = argparse.ArgumentParser(description='Pass arguments if necessary')

parser.add_argument('-url', required=True, help='target url')
parser.add_argument('-user', default="", help='username if you want to login')
parser.add_argument('-password', default="", help='password if you want to login')


args = parser.parse_args()


inputs = getAllInputFields(url=args.url)
inputFieldNames = inputFieldNames(inputs)
inputFieldLabels = inputFieldLabels(inputFieldNames)

findLoginFieldsAndLogin(browser, inputFieldNames, inputFieldLabels, url=args.url, user=args.user, password=args.password)		
findLoginButtonAndClick(browser)
time.sleep(1)

injectPayload("xss-top500.txt", url=args.url)
