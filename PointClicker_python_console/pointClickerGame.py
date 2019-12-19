def factor(i):
	return i ** 3.1

class PointClickerGame:
	def __init__(self):
		self.upgrades_capacity = 25
		self.score = 0
		self.pps = 0
		self.upgrades = list()
		self.upgrades_description = list()
		self.upgrades_amount = list()
		self.upgrades_cost = list()

		self.upgrades.append("Click!")
		upgrades_description.append("+1 point.")
		upgrades_cost.append(0)

		for i in range(1, self.upgrades_capacity):
			upgrades.append("Autoclick" + str(i))
			upgrades_description.append("+" + str(factor(i) * 10) + "pps.")
			upgrades_cost.append(factor(i) * 150)

	def command(self, n):
		if(n == 0):
			self.upgrades_amount[0] += 1
			self.score += 1
		else:
			tmp = factor(n) * 150
			if(self.score < tmp):
				return
			self.upgrades_amount[n] += 1
			self.score -= tmp
			self.pps += tmp / 15

	def add_pps():
		self.score += self.pps

	def save():
		f = open("save.txt", 'w')
		f.write(str(self.score) + '\n' + str(self.pps) + '\n')
		for i in range(0, self.upgrades_capacity):
			f.write(str(self.upgrades_amount[i]) + '\n')
		f.close()

	def load():
		f = open("save.txt", 'r')
		self.score = f.readline()
		self.pps = f.readline()
		for i in range(0, self.upgrades_capacity):
			self.upgrades_amount[i] = f.readline()
		f.close()
		