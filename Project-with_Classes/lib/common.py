import requests

def try_except(conn):
	try:
		conn
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
	except requests.KeyboardInterrupt as e:
		print(f"Keyboard Interrupt\n{str(e)}")
	except Exception as e:
		print(str(e))

def getID():
	id = int(input("Enter ID of a person: "))
	return id

def getData():
	id = int(input("Enter ID: "))
	first_name = input("Enter FIrst_Name: ")
	middle_name = input("Enter Middle_Name: ")
	last_name = input("Enter Last_Name: ")
	date_of_birth = input("Enter DOB(dd/mm/yyyy): ")
	data = {'id': id, 'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name, 'date_of_birth': date_of_birth}
	return data