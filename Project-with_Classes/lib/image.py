import requests
import json
from common import try_except
# from PIL import Image


class Image:
	def __init__(self):
		self.domain = "http://httpbin.org"
		self.path = "image"

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
		self.img_req = requests.get(f"{self.domain}/{self.path}/{self.type}")

		try_except(self.img_req)

		with open(f"../logs/{self.type}_image.{self.type}", "wb") as image:
			image.write(self.img_req.content)
			print("------------------------------------------------------------------------")
			print("Downloaded the image")
			print("------------------------------------------------------------------------")

	def imageMain(self):
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