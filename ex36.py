from sys import exit
from time import sleep
def start():
	print("What do u want?")
	start_code = input("Start a 'new game' or 'flee'? ")
	while start_code:

		if start_code == "new game":
			new_game()
			break
		elif start_code == "flee":
			exit("It is the end of the road. Bye!")
		else:
			print("I dont like it")
			start_code = input("So..?")

def new_game():
	print("You are in a cave")

	val = False
	while val is False:
		a_or_b = input("You've 2 options, go 'right' or 'left'.")
		if a_or_b == "right":
			exit("There is a hole, and you fell of. So. Byeeeeeeeeeeeeeee")
		elif a_or_b == "left":
			print("You've found the exit!")
			if 1:
				sleep(1)
				exit("\n \nJoke, the cave collapsed. Bye.")
		else:
			print("There is no escape!")


start()