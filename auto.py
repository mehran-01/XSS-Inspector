import requests
from bs4 import BeautifulSoup
import time
import argparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class AutoXSSTester():
	def __init__(self, browser):
		self.browser = browser


	#get all input fields to find crdentials login fields
	def getAllInputFields(self, url, url_login):
		#removing / if url included / at the end
		if url[-1] == "/":
			url = url[:-1]
		#make /login the default login page
		if not url_login:
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
		if htmlForm:
			inputs = htmlForm.find_all('input', type=["text", "password"])
			return inputs
		else:
			print("wasn't able to scrape the login form")

	#Extract Input Field Names
	def inputFieldNames(self, inputs):
		inputFieldNames = []
		for items in inputs:
			if items.has_attr('name'):
				inputFieldNames.append(items['name'])
		return inputFieldNames



	#extract input field labels
	def inputFieldLabels(self, inputFieldNames):
		inputFieldLabels = []
		for i in range(len(inputFieldNames)):
			input_tag = inputs[i].parent.text.encode('utf-8').strip()
			input_label_text = BeautifulSoup(input_tag, 'html.parser').get_text().lower()
			inputFieldLabels.append(input_label_text)
		return inputFieldLabels


	#find login fields to pass credentials to
	def findLoginFieldsAndLogin(self,inputFieldNames, inputFieldLabels, url, url_login, user, password): 
		#removing / if url included / at the end
		if url[-1] == "/":
			url = url[:-1]
		#make /login the default login page
		if not url_login:
			url_login = url + "/login"
		#browse to login url
		self.browser.get(url_login) 
		for i in range(len(inputFieldLabels)):
			if "user" in inputFieldNames[i] or "user" in inputFieldLabels[i] or "email" in inputFieldNames[i] or "email" in inputFieldLabels[i]:
				self.browser.find_element_by_name(inputFieldNames[i]).send_keys(user)
				if user:
					print("user passed to try to login")
			if "pass" in inputFieldNames[i] or "pass" in inputFieldLabels[i]:
				self.browser.find_element_by_name(inputFieldNames[i]).send_keys(password)
				if password:
					print("password passed to try to login")
		#find submit button and click to login
		try:
			login_attempt = self.browser.find_element_by_xpath("""//input[@type='submit']""")
			print("submit input clicked")
			login_attempt.submit()
			print("logged in")
		except:
			try:
				login_attempt = self.browser.find_element_by_xpath("""//button[@type='submit']""")
				print("submit button clicked")
				#add a delay to not login immediately after credentials entered otherwise might recognize as a bot!
				time.sleep(2)
				login_attempt.submit()
				print("logged in")
			except:
				# print("didn't login")
				pass



	#handle if alert pops up to be able to go to the next payload
	def handleAlert(self, url, payload, line):
		newurl = str(url)+"/"+str(payload)
		self.browser.get(newurl);
		try:
		    WebDriverWait(self.browser, 2).until(EC.alert_is_present(),
		                                   'Timed out waiting for PA creation ' +
		                                   'confirmation popup to appear.')

		    alert = self.browser.switch_to.alert
		    time.sleep(2)
		    alert.accept()
		    print("alert popped up and accepted")
	   	except: 
	  		pass



	#injecting top500 xss scripts to the target
	def injectPayload(self, payloads, url):
		#Create a CSV to put injected result in it
		f = open('result.csv','w')
		#Loop through XSS payloads to inject one by one
		with open(payloads, "r") as pl:
			print("started injecting payloads:")
		  	for line, payload in enumerate(pl, 1):
		  		#Click if an alert/popup script passed to be able to go next one
		  		self.handleAlert(url, payload, line)
		  		current_url = self.browser.current_url
			  	r = requests.get(current_url)
			  	payload_counter = line
			  	if payload.rstrip('\n') in r.content or payload.rstrip('\n').replace("\\", "/") in r.content:
			  		#print in terminal
			  		print("payload #"+ str(payload_counter) + " was injected: " + payload)
			  		#store in CSV
					f.write("payload #"+ str(payload_counter) + " was injected: " + payload+'\n')
			  	else:
			  		#print in terminal
			  		print("payload "+ str(payload_counter) +" was not injected!")
			f.close()



#pass Firefox driver
xss = AutoXSSTester(webdriver.Firefox())

#Create arguments commands
parser = argparse.ArgumentParser(description='Pass arguments if necessary')
#Required argument
requiredArgs =  parser.add_argument_group('required argument(s)')
requiredArgs.add_argument('-url', help='target url', required=True)
#Optional argument
parser.add_argument('-login', default="", help="login url if you want to login and it's not target url/login")
parser.add_argument('-user', default="", help='username if you want to login')
parser.add_argument('-password', default="", help='password if you want to login')


args = parser.parse_args()

if args.user and args.password:
	inputs = xss.getAllInputFields(url=args.url, url_login=args.login)
	inputFieldNames = xss.inputFieldNames(inputs)
	inputFieldLabels = xss.inputFieldLabels(inputFieldNames)
	#Search for login button and login
	xss.findLoginFieldsAndLogin(inputFieldNames, inputFieldLabels, url=args.url, url_login=args.login, user=args.user, password=args.password)		
	#give it some time to login(not super fatst to be caught!)
	time.sleep(2)
else:
	print("user and password didn't pass so didn't login")
#Pass payloads to inject to the target
xss.injectPayload("xss-top500.txt", url=args.url)
