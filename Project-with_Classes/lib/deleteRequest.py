import requests
import json
from common import try_except, getID

class DeleteStudentData:

	def __init__(self, domain, path):
		self.domain = domain
		self.path = path


	def deleteStudent(self):
		self.id = getID()
		self.del_req = requests.delete(f"{self.domain}/{self.path}/{self.id}")

		try_except(self.del_req)

		if(self.del_req.status_code == 200):
			self.del_req = json.loads(self.del_req.text)
			if(self.del_req['status'] == 'true'):
				print("------------------------------------------------------------------------")
				print("Data deleted")
				print("------------------------------------------------------------------------")
			else:
				print("------------------------------------------------------------------------")
				print(self.del_req['msg'])
				print("------------------------------------------------------------------------")
		else:
			print("------------------------------------------------------------------------")
			print(self.del_req.status_code)
			print("------------------------------------------------------------------------")


	def deleteMain(self):
		while True:
			print("----------------In deleteMain----------------")
			self.request = input(("Do you want to delete any other data(Y/y or N/n): "))

			if(self.request == 'Y' or self.request == 'y'):
				self.deleteStudent()
				continue
			elif(self.request == 'N' or self.request == 'n'):
				break
			else:
				print("Invalid option, press only Y/y or N/n")