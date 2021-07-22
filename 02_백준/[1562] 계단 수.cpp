// https://www.acmicpc.net/problem/1562


#include <iostream>
#include <cstring>

using namespace std;
typedef long long ll;

const ll KEY = 1000000000LL;

int main() {
	int n;
	ll answer = 0;
	ll dp[2][10][1 << 10];

	cin >> n;
	memset(dp, 0, sizeof(dp));

	for (int k = 0; k < 10; k++)
		dp[0][k][1 << k] = 1;

	int i = 0;
	int j = 1;

	while (--n) {
		for (int p = 0; p < 10; p++) {
			for (int q = 1; q < 1024; q++) {
				int r = q | (1 << p);

				if (0 < p)	dp[j][p][r] += dp[i][p - 1][q];
				if (p < 9)	dp[j][p][r] += dp[i][p + 1][q];
				dp[j][p][r] %= KEY;
			}
		}

		for (int p = 0; p < 10; p++)
			for (int q = 1; q < 1024; q++)
				dp[i][p][q] = 0;

		swap(i, j);
	}

	for (int k = 1; k < 10; k++) 
		answer = (answer + dp[i][k][1023]) % KEY;

	cout << answer << endl;

	return 0;
}
