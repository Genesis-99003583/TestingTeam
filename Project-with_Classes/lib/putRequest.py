import requests
import json
from common import try_except, getData, getID


class PutStudentData:

	def __init__(self, domain, path):
		self.domain = domain
		self.path = path


	def putStudent(self):
		self.data = getData()
		self.id = self.data['id']
		self.put_req = requests.put(f"{self.domain}/{self.path}/{self.id}", json=self.data)

		try_except(self.put_req)

		if(self.put_req.status_code == 200):
			print("------------------------------------------------------------------------")
			print("Data updated")
			print("------------------------------------------------------------------------")
		elif(self.put_req.status_code == 404):
			print("------------------------------------------------------------------------")
			print("ID not found")
			print("------------------------------------------------------------------------")
		else:
			print("------------------------------------------------------------------------")
			print(self.put_req.status_code)
			print("------------------------------------------------------------------------")


	def putMain(self):
		while True:
			print("----------------In putMain----------------")

			self.request = input(("Do you want to update any other data(Y/y or N/n): "))

			if(self.request == 'Y' or self.request == 'y'):
				self.putStudent()
				continue
			elif(self.request == 'N' or self.request == 'n'):
				break
			else:
				print("Invalid option, press only Y/y or N/n")