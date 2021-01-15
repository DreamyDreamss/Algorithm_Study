#include <iostream>
#include <cmath>

using namespace std;

int N;
int col[15];
int result = 0;

void queen(int n) {
    int flag = 0;

    if (n == N) {
        result++;
        
    }
    else {
        for (int i = 0; i < N; i++) {

            col[n] = i  ;
            for (int j = 0; j < n; j++) {
                
                if (col[j] == col[n] || (n - j) == abs(col[n] - col[j])) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) queen(n + 1);
            else flag = 0;
        }
    }
    
}
int main() {
    cin >> N;
    queen(0);
    cout << result << endl;
}