#include <iostream>

using namespace std;

int main() {
	int N, K;
	int coin[10];
    
	cin >> N >> K;
    
	for (int i = 0; i < N; i++) cin >> coin[i];
    
	int m = N - 1;
	int cnt = 0;
    
	while (1) {
		if (K == 0) break;

		if (K / coin[m] >= 1) {
			cnt += K / coin[m];
			K = K % coin[m];
		}
		m--;
	}
	cout << cnt;
}