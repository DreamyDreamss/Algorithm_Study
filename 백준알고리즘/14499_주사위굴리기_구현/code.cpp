#include <iostream>
#define UP 3
#define DOWN 4
#define RIGHT 1
#define LEFT 2

using namespace std;

int dice[5][4] = { 0 };
int map[21][21] = { 0 };
int n, m;
int posX, posY;

void print() {
	cout << dice[1][1] << "\n";
}

void movedown() {

	if (posX + 1 >= n) return;
	posX++;

	int tmp = dice[3][1];

	for (int i = 3; i > 0; i--) {
		dice[i][1] = dice[i - 1][1];
	}
	dice[0][1] = tmp;

	if (map[posX][posY] == 0) {
		map[posX][posY] = dice[3][1];
	}
	else {
		dice[3][1] = map[posX][posY];
		map[posX][posY] = 0;
	}
	print();
}

void moveup() {

	if (posX - 1 < 0) return;
	posX--;

	int tmp = dice[0][1];

	for (int i = 0; i < 3; i++) {
		dice[i][1] = dice[i + 1][1];
	}
	dice[3][1] = tmp;

	if (map[posX][posY] == 0) {
		map[posX][posY] = dice[3][1];
	}
	else {
		dice[3][1] = map[posX][posY];
		map[posX][posY] = 0;
	}
	print();
}

void moveleft() {

	if (posY - 1 < 0) return;
	posY--;

	int floortmp = dice[3][1];
	int lefttmp = dice[1][0];

	for (int i = 0; i < 2; i++) {
		dice[1][i] = dice[1][i+1];
	}
	dice[1][2] = floortmp;
	dice[3][1] = lefttmp;

	if (map[posX][posY] == 0) {
		map[posX][posY] = dice[3][1];
	}
	else {
		dice[3][1] = map[posX][posY];
		map[posX][posY] = 0;
	}
	print();
}

void moveright() {

	if (posY + 1 >= m) return;
	posY++;

	int floortmp = dice[3][1];
	int righttmp = dice[1][2];

	for (int i = 2; i > 0 ; i--) {
		dice[1][i] = dice[1][i-1];
	}
	dice[1][0] = floortmp;
	dice[3][1] = righttmp;

	if (map[posX][posY] == 0) {
		map[posX][posY] = dice[3][1];
	}
	else {
		dice[3][1] = map[posX][posY];
		map[posX][posY] = 0;
	}
	print();
}
int main() {

	int order;

	cin >> n >> m >> posX >> posY >> order;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}

	for (int i = 0; i < order; i++) {
		int direction;
		cin >> direction;
		switch (direction)
		{
		case UP: {
			moveup();
			break;
		}
		case DOWN: {
			movedown();
			break;
		}
		case LEFT: {
			moveleft();
			break;
		}
		case RIGHT: {
			moveright();
			break;
		}
		default:
			break;
		}
	}
}
