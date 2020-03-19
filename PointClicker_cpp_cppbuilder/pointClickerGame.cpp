#include "pointClickerGame.h"

uint64_t factor(double_t i) {
	return pow(i, 3.1);
}

std::string* PointClickerGame::get_upgrades() {
	return upgrades;
}

std::string* PointClickerGame::get_upgrades_description() {
	return upgrades_description;
}

uint64_t* PointClickerGame::get_upgrades_cost() {
	return upgrades_cost;
}

uint64_t PointClickerGame::get_pps() {
	return pps;
}

uint64_t* PointClickerGame::get_upgrades_amount() {
	return upgrades_amount;
}

PointClickerGame::PointClickerGame() {
	score = 0;
	pps = 0;
	upgrades_init();
}

void PointClickerGame::save() {
	fout.open("save.txt");
	fout << score << std::endl << pps << std::endl;
	for (uint8_t i = 0; i < upgrades_capacity; i++) {
		fout << upgrades_amount[i] << std::endl;
	}
	fout.close();
}

void PointClickerGame::load() {
	fin.open("save.txt");
	fin >> score >> pps;
	for (uint8_t i = 0; i < upgrades_capacity; i++) {
		fin >> upgrades_amount[i];
	}
	fin.close();
}

void PointClickerGame::upgrades_init() {
	upgrades[0] = "Click!";
	upgrades_description[0] = "+1 point.";
	upgrades_cost[0] = 0;
	for (uint8_t i = 1; i < upgrades_capacity; i++) {
		upgrades[i] = "Autoclick" + std::to_string(i);
		upgrades_description[i] = "+" + std::to_string(factor(i) * 10) + "pps.";
		upgrades_cost[i] = factor(i) * 150;
	}
}

void PointClickerGame::command(uint8_t n) {
	if (n == 0) {
		upgrades_amount[0]++;
		score++;
	}
	else {
		uint64_t tmp = factor(n) * 150;
		if (score < tmp)
			return;
		upgrades_amount[n]++;
		score -= tmp;
		pps += tmp / 15;
	}
}

void PointClickerGame::add_pps() {
	score += pps;
}

uint64_t PointClickerGame::get_score() {
	return score;
}

PointClickerGame::~PointClickerGame() {

}
