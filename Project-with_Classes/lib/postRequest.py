import requests
import json
from common import try_except, getData


class PostStudentData:

	def __init__(self, domain, path):
		self.domain = domain
		self.path = path


	def postStudent(self):
		self.data = getData()
		self.post_req = requests.post(f"{self.domain}/{self.path}", json=self.data)

		try_except(self.post_req)

		if(self.post_req.status_code == 201):
			print("------------------------------------------------------------------------")
			print(f"Data added\n{self.post_req.text}")
			print("------------------------------------------------------------------------")
		else:
			print("------------------------------------------------------------------------")
			print(self.post_req.status_code)
			print("------------------------------------------------------------------------")


	def postMain(self):
		while True:
			print("----------------In postMain----------------")

			self.request = input(("Do you want to add any other data(Y/y or N/n): "))

			if(self.request == 'Y' or self.request == 'y'):
				self.postStudent()
				continue
			elif(self.request == 'N' or self.request == 'n'):
				break
			else:
				print("Invalid option, press only Y/y or N/n")