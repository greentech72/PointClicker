#pragma once
#ifndef POINTCLICKERGAME_H
#define POINTCLICKERGAME_H

#include <string>
#include <fstream>

static uint64_t factor(double_t);

class PointClickerGame {
public:
	static const uint8_t upgrades_capacity = 25;

	PointClickerGame();
	~PointClickerGame();
	void command(uint8_t);
	void add_pps();
	uint64_t get_score();

	std::string* get_upgrades();
	std::string* get_upgrades_description();
	uint64_t* get_upgrades_cost();
	uint64_t get_pps();
	uint64_t* get_upgrades_amount();

	void save();
	void load();

private:
	std::fstream fout;
	std::ifstream fin;

	uint64_t score;
	uint64_t pps;

	std::string upgrades[upgrades_capacity];
	std::string upgrades_description[upgrades_capacity];
	uint64_t upgrades_amount[upgrades_capacity];
	uint64_t upgrades_cost[upgrades_capacity];

	void upgrades_init();
};

#endif // POINTCLICKERGAME_H
