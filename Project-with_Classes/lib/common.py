import requests


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


def try_except(fun):
	def handling(*args, **kwargs):
		try:
			fun(*args, **kwargs)
		except requests.exceptions.ConnectionError as e:
			print(f"Connection Error. Make sure you are connected to Internet.\n{e}")
		except requests.exceptions.Timeout as e:
			print(f"Request Timeout\n{e}")
		except requests.exceptions.ReadTimeout as e:
			print(f"The server did not send any data in the allotted amount of time.\n{e}")
		except requests.exceptions.URLRequired as e:
			print(f"A valid URL is required to make a request.\n{e}")
		except requests.exceptions.HTTPError as e:
			print(f"Error 404: Page not found, check the link & try again\n{e}")
		except Exception as e:
			print(e)
	return handling