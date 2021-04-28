import requests
import json
# import os
import sys
sys.path.append("../lib")

from getRequest import getMain
from putRequest import putMain
from postRequest import postMain
from deleteRequest import deleteMain
from image import imageMain

domain = "http://thetestingworldapi.com"
path = "api/studentsDetails"


if __name__ == '__main__':
	while True:
		print("----------------In Main----------------")
		request = int(input("1. GET\n2. POST\n3. PUT\n4. DELETE\n5. Download Image\n6. Exit\nSelect anything from 1 to 6: "))
		if(request == 1):
			# os.system('python ../lib/getRequest.py')
			getMain(domain, path)
		elif(request == 2):
			# os.system('python ../lib/postRequest.py')
			postMain(domain, path)
		elif(request == 3):
			# os.system('python ../lib/putRequest.py')
			putMain(domain, path)
		elif(request == 4):
			# os.system('python ../lib/deleteRequest.py')
			deleteMain(domain, path)
		elif(request == 5):
			imageMain()
		elif(request == 6):
			exit()
		else:
			print("Invalid option(Select only from 1 to 5)")