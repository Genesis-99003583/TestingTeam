# import sys
# sys.path.append("../bin")

# import main

import requests
import json

def putStudent(domain, path, id, data):
	try:
		put_req = requests.put(f"{domain}/{path}/{id}", json=data)
		# print(put_req.url)
	except Exception as e:
		raise e

	if(put_req.status_code == 200):
		print("Data updated")
	else:
		print(put_req.status_code)


def putMain(domain, path):
	while True:
		print("----------------In putMain----------------")
		id = int(input("Enter ID: "))
		first_name = input("Enter FIrst_Name: ")
		middle_name = input("Enter Middle_Name: ")
		last_name = input("Enter Last_Name: ")
		date_of_birth = input("Enter DOB(dd/mm/yyyy): ")
		data = {'id': id, 'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name, 'date_of_birth': date_of_birth}
		# print(data)
		# id = 209768
		putStudent(domain, path, id, data)

		request = input(("Do you want to update any other data(Y/y or N/n): "))

		if(request == 'Y' or request == 'y'):
			continue
		elif(request == 'N' or request == 'n'):
			break
		else:
			print("Invalid option, press only Y/y or N/n")