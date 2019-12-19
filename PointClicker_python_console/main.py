from pointclickergame import *
from os import system
from time import time

pcg = pointclickergame()

def Menu():
	system("cls")
	print("Your score :", pcg.score)
	for upg in pcg.upgrades:
		print(upg.name, "[" + str(upg.amount) + "]",upg.description, upg.cost)
	n = input("What do you want to do > ")
	return n


if __name__ == '__main__':
	system("color 02")
	for i in range(0, 100):
		pcg.command(0)
	while(1):

		n = Menu()
		if(n == '-1'):
			exit()

		try:
			pcg.command(int(n) - 1)
		except:
			continue
		pcg.add_pps()