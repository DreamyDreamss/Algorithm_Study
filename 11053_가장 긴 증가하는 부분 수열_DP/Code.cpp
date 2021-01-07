#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dp[1001] = { 0 };
int result = 1;

int main() {

	int N;
	vector<int> arr;

	cin >> N;

	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		arr.push_back(tmp);
	}

	for (int i = 0; i < arr.size(); i++) {
        dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (arr[i] > arr[j]) {
				dp[i] = max(dp[j] + 1, dp[i]);
				result = max(result, dp[i]);
			}
		}
	}

	cout << result;
}