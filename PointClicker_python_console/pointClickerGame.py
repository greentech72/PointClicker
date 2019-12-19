def factor(n):
    return int(n ** 3.1)

class upgrade:
    def __init__(self, name, description, amount, cost):
        self.name = name
        self.description = description
        self.amount = amount
        self.cost = cost

class pointclickergame:
    def __init__(self):
        self.upgrades_capacity = 25
        self.score = 0
        self.pps = 0
        self.upgrades = []
        self.upgrades.append(upgrade("Click!", "+1 point", 0, 0))
        for i in range(1, self.upgrades_capacity):
            self.upgrades.append(upgrade("Autoclick" + str(i), "+" + str(factor(i) * 10) + "pps.", 0, factor(i) * 150))

    def command(self, n):
        if(n == 0):
            self.upgrades[0].amount += 1
            self.score += 1
        else:
            tmp = factor(n) * 150
            if(self.score < tmp):
                return
            self.upgrades[n].amount += 1
            self.score -= tmp
            self.pps += tmp / 15

    def add_pps(self):
        self.score += self.pps

    def save(self):
        f = open("save.txt", 'w')
        f.write(str(int(self.score)) + "\n" + str(int(self.pps)) + "\n")
        for i in range(0, self.upgrades_capacity):
            f.write(str(self.upgrades[i].amount) + "\n")
        f.close()

    def load(self):
        f = open("save.txt", 'r')
        self.score = int(f.readline())
        self.pps = int(f.readline())
        for i in range(0, self.upgrades_capacity):
            self.upgrades[i].amount = int(f.readline())
        f.close()