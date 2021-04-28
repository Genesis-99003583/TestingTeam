import sys
sys.path.append("../lib")

from getRequest import GetStudentData
from putRequest import PutStudentData
from postRequest import PostStudentData
from deleteRequest import DeleteStudentData
from image import Image

domain = "http://thetestingworldapi.com"
path = "api/studentsDetails"


if __name__ == '__main__':
	while True:
		print("----------------In Main----------------")
		request = int(input("1. GET\n2. POST\n3. PUT\n4. DELETE\n5. Download Image\n6. Exit\nSelect anything from 1 to 6: "))
		if(request == 1):
			getStudData = GetStudentData(domain, path)
			getStudData.getMain()
		elif(request == 2):
			postStudData = PostStudentData(domain, path)
			postStudData.postMain()
		elif(request == 3):
			putStudData = PutStudentData(domain, path)
			putStudData.putMain()
		elif(request == 4):
			delStud = DeleteStudentData(domain, path)
			delStud.deleteMain()
		elif(request == 5):
			imageData = Image()
			imageData.imageMain()
		elif(request == 6):
			exit()
		else:
			print("Invalid option(Select only from 1 to 6)")