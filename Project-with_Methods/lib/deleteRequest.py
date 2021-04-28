# import sys
# sys.path.append("../bin")

# import main

import requests
import json

def deleteStudent(domain, path, id):
	try:
		del_req = requests.delete(f"{domain}/{path}/{id}")
		# print(del_req.url)
	except Exception as e:
		raise e

	if(del_req.status_code == 200):
		del_req = json.loads(del_req.text)
		if(del_req['status'] == 'true'):
			print("Data deleted")
		else:
			print(del_req['msg'])
	else:
		print(del_req.status_code)


def deleteMain(domain, path):
	while True:
		print("----------------In deleteMain----------------")
		id = int(input("Enter ID of a person: "))
		deleteStudent(domain, path, id)
		request = input(("Do you want to delete any other data(Y/y or N/n): "))

		if(request == 'Y' or request == 'y'):
			continue
		elif(request == 'N' or request == 'n'):
			break
		else:
			print("Invalid option, press only Y/y or N/n")