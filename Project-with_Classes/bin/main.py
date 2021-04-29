import sys
sys.path.append("../lib")
import yaml

from exec import StudentData

with open(r'config.yaml') as configFile:
	data = yaml.load(configFile, Loader = yaml.FullLoader)
	domain = data['domain']
	path = data['path']


if __name__ == '__main__':
	studData = StudentData(domain=domain, path=path)
	while True:
		print("----------------In Main----------------")
		request = int(input("1. GET\n2. POST\n3. PUT\n4. DELETE\n5. Download Image\n6. Exit\nSelect anything from 1 to 6: "))
		if(request == 1):
			studData.getMain()
		elif(request == 2):
			studData.postMain()
		elif(request == 3):
			studData.putMain()
		elif(request == 4):
			studData.deleteMain()
		elif(request == 5):
			studData.imageMain()
		elif(request == 6):
			exit()
		else:
			print("Invalid option(Select only from 1 to 6)")