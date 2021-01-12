#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dp[101][100000] = { 0 };

int main() {

	int N, K;
	

	cin >> N >> K;
	vector<pair<int, int>> info(N+1);

	for (int i = 1; i <= N; i++) cin >> info[i].first >> info[i].second;

	for (int i = 1; i <= N; i++) {

		int w = info[i].first, v = info[i].second;

		for (int j = 0; j <= K; j++) {
			if (j < w) dp[i][j] = dp[i - 1][j];
			else dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v);
		}
	}

	cout << dp[N][K];
}