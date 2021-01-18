#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	int N;
	int maxValue = 0;
	vector<int> arr;

	cin >> N;

	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		if (tmp > maxValue) {
			maxValue = tmp;
		}
		arr.push_back(tmp);
	}

	int M;
	cin >> M;

	int left = 0;
	int right = maxValue;
	int result = 0;

	while (left <= right) {

		int mid = (left + right) / 2;
		int sum = 0;
		for (int i = 0; i < N; i++) {
			if (mid >= arr[i]) sum += arr[i];
			else sum += mid;
		}
		if (sum > M) {
			right = mid - 1;
		}
		else {
			left = mid + 1;
			if (sum > result) {
				result = mid;
			}
		}
	}

	cout << result;
}