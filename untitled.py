for i in range(len(inputFieldNames)):
	browser.find_element_by_name(inputFieldNames[i]).send_keys("demo123")

print(inputFieldLabels)




form = browser.find_element_by_tag_name("form")
form_text = browser.find_element_by_xpath("""//input[@type='text']""")

print(form_text)



with open("payloads.txt", "r") as ins:
    payloads = []
    for line in ins:
        payloads.append(line)


current_url = browser.current_url


for x in range(len(payloads)):
	newurl = current_url+payloads[x]
	browser.get(newurl);
	time.sleep(5)