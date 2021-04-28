# import sys
# sys.path.append("../bin")

# import main

import requests
import json

def postStudent(domain, path, data):
	try:
		post_req = requests.post(f"{domain}/{path}", json=data)
		# print(post_req.url)
	except Exception as e:
		raise e

	if(post_req.status_code == 201):
		print(f"Data added\n{post_req.text}")
	else:
		print(post_req.status_code)

# def particularStudent(id):
# 	get_req = requests.get(f"{domain}/{path}/{id}")
# 	# print(get_req)

# 	get_req = json.loads(get_req.text)

# 	print("----------------Particular Student----------------")
# 	# print(get_req)
# 	print(get_req)


def postMain(domain, path):
	while True:
		print("----------------In postMain----------------")
		id = int(input("Enter ID: "))
		first_name = input("Enter FIrst_Name: ")
		middle_name = input("Enter Middle_Name: ")
		last_name = input("Enter Last_Name: ")
		date_of_birth = input("Enter DOB(dd/mm/yyyy): ")
		data = {'id': id, 'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name, 'date_of_birth': date_of_birth}
		# print(data)
		# id = 209768
		postStudent(domain, path, data)

		request = input(("Do you want to add any other data(Y/y or N/n): "))

		if(request == 'Y' or request == 'y'):
			continue
		elif(request == 'N' or request == 'n'):
			break
		else:
			print("Invalid option, press only Y/y or N/n")
	# data = {'id': 99003583, 'first_name': 'Abhishek', 'middle_name': 'Reddy', 'last_name': 'Kavali', 'date_of_birth': '29/10/1997'}
	# postStudent(domain, path, data)
	# particularStudent(99003583)