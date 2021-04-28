import requests
import json
# from PIL import Image


def downloadImage(type):
	try:
		img_req = requests.get(f"http://httpbin.org/image/{type}")
	except Exception as e:
		raise e

	with open(f"../logs/{type}_image.{type}", "wb") as image:
		image.write(img_req.content)
		print("Downloaded the image")

	# print("Do you want to open Image(Y/y or N/n): ")
	# if(request == 'Y' or request == 'y'):
	# 	Image.open(f"../logs/{type}_image.{type}")
	# elif(request == 'N' or request == 'n'):
	# 	break
	# else:
	# 	print("Invalid option, press only Y/y or N/n")

def imageMain():
	while True:
		print("----------------In imageMain----------------")
		request = int(input("1. PNG\n2. JPEG\n3. SVG\n4. WEBP\nWhat type of image you want(Select anything from 1 to 4): "))
		if(request == 1):
			downloadImage("png")
		elif(request == 2):
			downloadImage("jpeg")
		elif(request == 3):
			downloadImage("svg")
		elif(request == 4):
			downloadImage("webp")

		request = input(("Do you want to download any other image(Y/y or N/n): "))

		if(request == 'Y' or request == 'y'):
			continue
		elif(request == 'N' or request == 'n'):
			break
		else:
			print("Invalid option, press only Y/y or N/n")

# 			

# response = requests.get("http://httpbin.org/image/png")
# print(response['data'])

# with open("../logs/image.png", "wb") as image:
# 	image.write(response.content)