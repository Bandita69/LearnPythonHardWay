from sys import exit
lamp_work = input("Is the lamp work?")
if str(lamp_work).lower() == "yes":
	exit("Lamp is working.")
elif str(lamp_work).lower() == "no":
	plugged_in = input("Is it plugged in?")
	if str(plugged_in).lower() == "no":
		exit("You should plug it in!")
	elif str(plugged_in).lower() == "yes":
		blub_burned = input("Is the blub burned out?")
		if str(blub_burned).lower() == "yes":
			exit("Replace it!")
		elif str(blub_burned).lower() == "no":
			exit("Repair the lamp!")