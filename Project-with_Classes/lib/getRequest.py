import requests
import json
from common import try_except, getID


class GetStudentData:

	def __init__(self, domain, path):
		self.domain = domain
		self.path = path

	def allStudents(self):
		self.get_req = requests.get(f"{self.domain}/{self.path}")

		try_except(self.get_req)

		self.get_req = json.loads(self.get_req.text)

		print("\n\n----------------All Students----------------")
		for i in self.get_req:
			print(i)
		print("------------------------------------------------------------------------")

	def particularStudent(self):
		self.id = getID()
		print("\n\n----------------Particular Student----------------")
		self.get_req = requests.get(f"{self.domain}/{self.path}/{self.id}")

		try_except(self.get_req)

		print("\n\n----------------Particular Student----------------")
		if(self.get_req.status_code == 200):
			self.get_req = json.loads(self.get_req.text)
			if(self.get_req['status'] == 'true'):
				print(self.get_req['data'])
			else:
				print(self.get_req['msg'])
		else:
			print(self.get_req.status_code)
		print("--------------------------------------------------")


	def getMain(self):
		while True:
			print("----------------In getMain----------------")
			request = int(input("1. All Students Data\n2. Particular Student Data\n3. Exit\nSelect anything from 1 to 3: "))
			if(request == 1):
				self.allStudents()
			elif(request == 2):
				self.particularStudent()
			elif(request == 3):
				break
			else:
				print("Invalid option(Select only from 1 to 3)")