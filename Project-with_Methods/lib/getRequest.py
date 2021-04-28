# import sys
# sys.path.append("../bin")

# import main

import requests
import json
# id = 209740

# jsonFile = open("../bin/config.json", 'r')
# link = json.loads(jsonFile)
# print(link)

def allStudents(domain, path):
	get_req = requests.get(f"{domain}/{path}")

	# print(get_req.url)

	get_req = json.loads(get_req.text)

	print("----------------All Students----------------")
	for i in get_req:
		print(i)

def particularStudent(domain, path, id):
	try:
		get_req = requests.get(f"{domain}/{path}/{id}")
		# get_req_status = get_req.status_code
	except Exception as e:
		raise e
	# print(get_req)

	# get_req = json.loads(get_req.text)

	print("\n\n----------------Particular Student----------------")
	# print(get_req)
	if(get_req.status_code == 200):
		get_req = json.loads(get_req.text)
		if(get_req['status'] == 'true'):
			print(get_req['data'])
		else:
			print(get_req['msg'])
		# print(get_req)
		# print(get_req_status)
	else:
		print(get_req.status_code)
	# print(get_req['data'])


def getMain(domain, path):
	while True:
		print("----------------In getMain----------------")
		request = int(input("1. All Students Data\n2. Particular Student Data\n3. Exit\nSelect anything from 1 to 3: "))
		if(request == 1):
			allStudents(domain, path)
		elif(request == 2):
			id = int(input("Enter ID of the person(eg: 209768): "))
			particularStudent(domain, path, id)
		elif(request == 3):
			break
		else:
			print("Invalid option(Select only from 1 to 3)")