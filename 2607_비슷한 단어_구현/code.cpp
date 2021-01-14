#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

	int info[27] = { 0 };
	int firstcnt = 0;
	int result = 0;
	vector<string> arr;
	string first;
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		string tmp;
		cin >> tmp;
		if (i == 0) first = tmp;
		else arr.push_back(tmp);
	}

	for (int i = 0; i < first.size(); i++) {
		info[first[i] - 65]++;
	}

	for (int i = 0; i < arr.size(); i++) {
		int errorcnt = 0;
		int cmp[27] = { 0 };
		int idx = 0;
		int x = 0;
		int y = 0;

		//비교 문자열 카운트배열 생성
		for (int j = 0; j < arr[i].size(); j++) {
			cmp[arr[i][j] - 65]++;
		}

		//원본 문자열과 비교 문자열 비교
		for (idx = 0; idx < 26; idx++) {
			if(abs(info[idx] - cmp[idx])>1) break;

			if (info[idx] != cmp[idx]){
				if (info[idx] > cmp[idx]) x++;
				else if(info[idx] < cmp[idx])y++;

				if (x > 1 || y > 1) break;
			}
		}
		if (idx == 26) {
			result++;
		}
	}
	cout << result;
}