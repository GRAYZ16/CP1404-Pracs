__author__ = "Joshua Gray"

name = input("Enter your name: ")

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

is_running = True

while is_running:
	print(MENU)
	command = input(">>> ").upper()

	if command == "H":
		print("Hello "+ name)
	elif command == "G":
		print("Goodbye " + name)
	elif command == "Q":
		print("Finished")
		is_running = False
	else:
		print("Invalid choice")