import requests
import json
from common import *

class StudentData:
	def __init__(self, domain, path):
		self.domain = domain
		self.path = path

	# ---------------------------------------GET Operations(Start)---------------------------------------

	def allStudents(self):

		try:
			self.get_req = requests.get(f"{self.domain}/{self.path}")
		except requests.exceptions.ConnectionError as e:
			print(f"Connection Error. Make sure you are connected to Internet.\n{str(e)}")
		except requests.exceptions.Timeout as e:
			print(f"Request Timeout\n{str(e)}")
		except requests.exceptions.ReadTimeout as e:
			print(f"The server did not send any data in the allotted amount of time.\n{str(e)}")
		except requests.exceptions.URLRequired as e:
			print(f"A valid URL is required to make a request.\n{str(e)}")
		except requests.exceptions.HTTPError as e:
			print(f"Error 404: Page not found, check the link & try again\n{str(e)}")
		except Exception as e:
			print(str(e))

		self.get_req = json.loads(self.get_req.text)

		print("\n\n----------------All Students----------------")
		for i in self.get_req:
			print(i)
		print("------------------------------------------------------------------------")

	def particularStudent(self):
		self.id = getID()

		try:
			self.get_req = requests.get(f"{self.domain}/{self.path}/{self.id}")
		except requests.exceptions.ConnectionError as e:
			print(f"Connection Error. Make sure you are connected to Internet.\n{str(e)}")
		except requests.exceptions.Timeout as e:
			print(f"Request Timeout\n{str(e)}")
		except requests.exceptions.ReadTimeout as e:
			print(f"The server did not send any data in the allotted amount of time.\n{str(e)}")
		except requests.exceptions.URLRequired as e:
			print(f"A valid URL is required to make a request.\n{str(e)}")
		except requests.exceptions.HTTPError as e:
			print(f"Error 404: Page not found, check the link & try again\n{str(e)}")
		except Exception as e:
			print(str(e))

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

	def postStudent(self):
		self.data = getData()

		try:
			self.post_req = requests.post(f"{self.domain}/{self.path}", json=self.data)
		except requests.exceptions.ConnectionError as e:
			print(f"Connection Error. Make sure you are connected to Internet.\n{str(e)}")
		except requests.exceptions.Timeout as e:
			print(f"Request Timeout\n{str(e)}")
		except requests.exceptions.ReadTimeout as e:
			print(f"The server did not send any data in the allotted amount of time.\n{str(e)}")
		except requests.exceptions.URLRequired as e:
			print(f"A valid URL is required to make a request.\n{str(e)}")
		except requests.exceptions.HTTPError as e:
			print(f"Error 404: Page not found, check the link & try again\n{str(e)}")
		except Exception as e:
			print(str(e))

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

	def putStudent(self):
		self.data = getData()
		self.id = self.data['id']

		try:
			self.put_req = requests.put(f"{self.domain}/{self.path}/{self.id}", json=self.data)
		except requests.exceptions.ConnectionError as e:
			print(f"Connection Error. Make sure you are connected to Internet.\n{str(e)}")
		except requests.exceptions.Timeout as e:
			print(f"Request Timeout\n{str(e)}")
		except requests.exceptions.ReadTimeout as e:
			print(f"The server did not send any data in the allotted amount of time.\n{str(e)}")
		except requests.exceptions.URLRequired as e:
			print(f"A valid URL is required to make a request.\n{str(e)}")
		except requests.exceptions.HTTPError as e:
			print(f"Error 404: Page not found, check the link & try again\n{str(e)}")
		except Exception as e:
			print(str(e))

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

	def deleteStudent(self):
		self.id = getID()

		try:
			self.del_req = requests.delete(f"{self.domain}/{self.path}/{self.id}")
		except requests.exceptions.ConnectionError as e:
			print(f"Connection Error. Make sure you are connected to Internet.\n{str(e)}")
		except requests.exceptions.Timeout as e:
			print(f"Request Timeout\n{str(e)}")
		except requests.exceptions.ReadTimeout as e:
			print(f"The server did not send any data in the allotted amount of time.\n{str(e)}")
		except requests.exceptions.URLRequired as e:
			print(f"A valid URL is required to make a request.\n{str(e)}")
		except requests.exceptions.HTTPError as e:
			print(f"Error 404: Page not found, check the link & try again\n{str(e)}")
		except Exception as e:
			print(str(e))

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

	def downloadImage(self):
		self.type = self.getType()

		try:
			self.img_req = requests.get(f"{self.imgDomain}/{self.imgPath}/{self.type}")
		except requests.exceptions.ConnectionError as e:
			print(f"Connection Error. Make sure you are connected to Internet.\n{str(e)}")
		except requests.exceptions.Timeout as e:
			print(f"Request Timeout\n{str(e)}")
		except requests.exceptions.ReadTimeout as e:
			print(f"The server did not send any data in the allotted amount of time.\n{str(e)}")
		except requests.exceptions.URLRequired as e:
			print(f"A valid URL is required to make a request.\n{str(e)}")
		except requests.exceptions.HTTPError as e:
			print(f"Error 404: Page not found, check the link & try again\n{str(e)}")
		except Exception as e:
			print(str(e))

		with open(f"../logs/{self.type}_image.{self.type}", "wb") as image:
			image.write(self.img_req.content)
			print("------------------------------------------------------------------------")
			print("Downloaded the image")
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