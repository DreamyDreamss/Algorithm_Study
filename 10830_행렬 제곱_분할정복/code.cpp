#include <iostream>

using namespace std;

typedef struct matrix {
	int info[5][5] = { 0 };
}matrix;

int N;
long long B;
matrix arr,arr2;

matrix multiple(matrix A, matrix B) {

	matrix result;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				result.info[i][j] += A.info[i][k] * B.info[k][j];
			}
			result.info[i][j] %= 1000;
		}
	}
	return result;
}

matrix divide(long long B) {

	if (B == 1) return arr;
	if (B == 2) return arr2;

	if (B % 2 == 0) {
		matrix temp = divide(B / 2);
		return multiple(temp,temp);
	}
	else {
		matrix temp = divide(B-1);
		return multiple(temp, arr);
	}
}
int main() {

	matrix ans;
	cin >> N >> B;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr.info[i][j];
		}
	}

	arr2 = multiple(arr, arr);

	ans = divide(B);
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << ans.info[i][j]%1000 << " ";
		}
		cout << '\n';
	}
}