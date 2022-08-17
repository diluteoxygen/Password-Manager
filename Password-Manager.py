def create():
	username = input("Enter your Username: ")
	password = input("Enter your Password: ")

	with open("database.txt", "a") as file:
		file.write(username+"|"+password+"\n")


def view():
	with open("database.txt", "r") as file:
		for line in file.readlines():
			data = (line.rstrip())
			usns, pwds = data.split("|")
			print("Username:", usns,"|	Password:", pwds)

def settings():
	pass
print("Password Manager:\n\n")
while True:
	method = input("Create[1] // View[2] // Settings[3] // Quit[4]: ")
	if method == "1":
		print("\n\n\nYou have selected [1] Create New Entry")
		a = input("================\n\n[C] to continue  \n[Q] to quit\n")
		if a.lower()=="q":
			break
		if a.lower()=="c":
			create()
		else:
			print("Invalid Entry")
			continue

	elif method == "2":
		pass
	elif method == "3":
		break
	else: 
		print("Invalid entry")
		continue

