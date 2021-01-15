#include <iostream>
#include <vector>
#include <algorithm>

#define VAL 9

using namespace std;

bool row[VAL][VAL+1];
bool col[VAL][VAL+1];
bool box[VAL][VAL+1];
int  sudoku[VAL][VAL];

void print() {

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cout << sudoku[i][j] << " ";
		}
		cout << '\n';
	}
}

void DFS(int cnt) {

	int x = cnt / VAL;
	int y = cnt % VAL;

	if (cnt == 81) {
		print();
		exit(0);
	}

	if (sudoku[x][y] == 0) {
		for (int i = 1; i <= 9; i++) {
			if (row[x][i] == false && col[y][i] == false && box[(x / 3)*3 +(y / 3)][i] == false) {
				col[y][i] = true;
				row[x][i] = true;
				box[(x / 3) * 3 + (y / 3)][i] = true;
				sudoku[x][y] = i;
				DFS(cnt + 1);
				col[y][i] = false;
				row[x][i] = false;
				box[(x / 3) * 3 + (y / 3)][i] = false;
				sudoku[x][y] = 0;
			}
		}
	}
	else {
		DFS(cnt + 1);
	}
}

int main() {
	
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> sudoku[i][j];
			if (sudoku[i][j] != 0) {
				row[i][sudoku[i][j]] = true;
				col[j][sudoku[i][j]] = true;
				box[(i / 3) * 3 + (j / 3)][sudoku[i][j]] = true;
			}
		}
	}
	DFS(0);

	
}