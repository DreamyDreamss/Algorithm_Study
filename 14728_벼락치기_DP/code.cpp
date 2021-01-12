#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	int N, T;
	int timeInfo[101] = { 0 };
	int scoreInfo[101] = { 0 };
	int dp[101][10001] = { 0 };

	cin >> N >> T;

	for (int i = 1; i <= N; i++) {
		cin >> timeInfo[i] >> scoreInfo[i];
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= T; j++) {

			int time = timeInfo[i];
			int score = scoreInfo[i];

			if (time > j) {
				dp[i][j] = dp[i - 1][j];
			}
			else {
				dp[i][j] = max(dp[i - 1][j], score + dp[i-1][j-time]);
			}
		}
	}
	/*
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= T; j++) {
			cout << dp[i][j] << " ";

		}
		cout << '\n' << '\n' << '\n';
	}*/

	cout << dp[N][T];
	

}