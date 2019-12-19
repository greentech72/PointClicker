from pointclickergame import *
from os import system

pcg = pointclickergame()

def MainMenu():
	system("cls")
	print("---------- POINT CLICKER ----------")
	print("1) Start new game")
	print("2) Load saved game")
	print("3) Exit")
	return int(input("Enter here > "))

def Menu():
	system("cls")
	print("Your score :", pcg.score)
	i = 0
	for upg in pcg.upgrades:
		print(str(i+1) + ")", upg.name, "[" + str(upg.amount) + "]",upg.description, upg.cost)
		i+=1
	return int(input("What do you want to do (-1 for save & exit) > "))

if __name__ == '__main__':
	system("color 02")
	n = MainMenu()
	while(True):
		if(n == 1):
			while(True):
				n = Menu()
				if(n == -1):
					pcg.save()
					exit()
				try:
					pcg.command(n - 1)
				except:
					continue
				pcg.add_pps()
		elif(n == 3):
			exit()
		elif(n == 2):
			pcg.load()
			n = 1
		else:
			n = MainMenu()