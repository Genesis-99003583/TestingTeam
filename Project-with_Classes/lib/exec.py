import json
from common import *

class StudentData:
	def __init__(self, domain, path):
		self.domain = domain
		self.path = path

	# ---------------------------------------GET Operations(Start)---------------------------------------

	@try_except
	def allStudents(self):
		self.get_req = requests.get(f"{self.domain}/{self.path}")

		self.get_req = json.loads(self.get_req.text)

		print("\n\n----------------All Students----------------")
		for i in self.get_req:
			print(i)
		print("------------------------------------------------------------------------")

	@try_except
	def particularStudent(self):
		self.id = getID()

		self.get_req = requests.get(f"{self.domain}/{self.path}/{self.id}")


		print("\n\n----------------Particular Student----------------")
		if(self.get_req.status_code == 200):
			self.get_req = json.loads(self.get_req.text)
			if(self.get_req['status'] == 'true'):
				print(self.get_req['data'])
			else:
				print(self.get_req['msg'])
		else:
			self.get_req = json.loads(self.get_req.text)
			print(self.get_req['Message'])
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

	# ---------------------------------------GET Operations(End)---------------------------------------

	# ---------------------------------------POST Operations(Start)---------------------------------------

	@try_except
	def postStudent(self):
		self.data = getData()

		self.post_req = requests.post(f"{self.domain}/{self.path}", json=self.data)


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

	# ---------------------------------------POST Operations(End)---------------------------------------

	# ---------------------------------------PUT Operations(Start)---------------------------------------

	@try_except
	def putStudent(self):
		self.data = getData()
		self.id = self.data['id']

		self.put_req = requests.put(f"{self.domain}/{self.path}/{self.id}", json=self.data)

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

	# ---------------------------------------PUT Operations(End)---------------------------------------

	# ---------------------------------------DELETE Operations(Start)---------------------------------------

	@try_except
	def deleteStudent(self):
		self.id = getID()

		self.del_req = requests.delete(f"{self.domain}/{self.path}/{self.id}")

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

	# ---------------------------------------DELETE Operations(End)---------------------------------------

	# ---------------------------------------IMAGE Download Operations(Start)---------------------------------------

	def getType(self):

		self.type = int(input("1. PNG\n2. JPEG\n3. SVG\n4. WEBP\nWhat type of image you want(Select anything from 1 to 4): "))
		if(self.type == 1):
			return "png"
		elif(self.type == 2):
			return "jpeg"
		elif(self.type == 3):
			return "svg"
		elif(self.type == 4):
			return "webp"
		else:
			print("Invalid option(Select only from 1 to 4)")
			self.getType()

	@try_except
	def downloadImage(self):
		self.type = self.getType()

		self.img_req = requests.get(f"{self.imgDomain}/{self.imgPath}/{self.type}")

		with open(f"../logs/{self.type}_image.{self.type}", "wb") as image:
			image.write(self.img_req.content)
			print("------------------------------------------------------------------------")
			print(f"Downloaded the image into \"logs\" folder as \"{self.type}_image.{self.type}\"")
			print("------------------------------------------------------------------------")

	def imageMain(self):
		self.imgDomain = "http://httpbin.org"
		self.imgPath = "image"
		while True:
			print("----------------In imageMain----------------")

			self.request = input(("Do you want to download any other image(Y/y or N/n): "))

			if(self.request == 'Y' or self.request == 'y'):
				self.downloadImage()
				continue
			elif(self.request == 'N' or self.request == 'n'):
				break
			else:
				print("Invalid option, press only Y/y or N/n")

	# ---------------------------------------IMAGE Download Operations(End)---------------------------------------