payloads = []

with open("payloads.txt", "r") as ins:
    payloads = []
    for line in ins:
        payloads.append(line)




for x in range(len(payloads)):
	newurl = "current_url"+"/"+payloads[x];
	print(newurl)