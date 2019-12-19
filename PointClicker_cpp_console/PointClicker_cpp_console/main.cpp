#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <ctime>
#include "pointClickerGame.h"

using namespace std;

PointClickerGame pcg; // Game Class

int MainMenu() {
	system("cls");
	cout << "---------- POINT CLICKER ----------" << endl;
	cout << "1) Start new game" << endl;
	cout << "2) Load saved game" << endl;
	cout << "3) Exit" << endl << endl;
	cout << "Enter here > ";
	int m;
	cin >> m;
	return m;
}

void Menu() {
	system("cls");
	cout << setw(25) << "Your points : " << pcg.get_score() << endl;
	cout << setw(25) << "Your pps : " << pcg.get_pps() << endl;
	string* u = pcg.get_upgrades();
	string* ud = pcg.get_upgrades_description();
	uint64_t* uc = pcg.get_upgrades_cost();
	uint64_t* ua = pcg.get_upgrades_amount();

	for (int i = 0; i < pcg.upgrades_capacity; i++) {
		cout << setw(20) << i + 1 << ") [" << ua[i] << "] " << u[i] << " " << ud[i] << " It'll cost : " << uc[i] << endl;
	}
	cout << endl;
	cout << setw(20) << "Enter what you want to do (-1 to save & exit) > ";
}

int main()
{
	system("color 02");

	int m = MainMenu();
	while(1) {
	
		if (m == 1) {
			while (true) {
				Menu();
				cin >> m;
				pcg.command(m - 1);
				if (m == -1) {
					pcg.save();
					exit(0);
				}
				pcg.add_pps();
			}
		}
		else if (m == 2) {
			pcg.load();
			m = 1;

		}
		else if (m == 3) {
			exit(0);
		}
		else {
			m = MainMenu();
		}
	}

	cout << endl;
	return 0;
}
