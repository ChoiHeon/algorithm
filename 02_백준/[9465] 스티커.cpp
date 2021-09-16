// 문제: https://www.acmicpc.net/problem/9465

#include <iostream>
#include <memory.h>
#include <algorithm>


int n;
int sticker[2][100001];
int dp[3][100001];

using namespace std;


void solve() {
	cin >> n;
	memset(dp, 0, sizeof(dp));


	for (int i = 0; i < 2; i++)
		for (int j = 1; j <= n; j++)
			cin >> sticker[i][j];

	for (int i = 1; i <= n; i++) {
		dp[0][i] = max(dp[1][i - 1], dp[2][i - 1]) + sticker[0][i];
		dp[1][i] = max(dp[0][i - 1], dp[2][i - 1]) + sticker[1][i];
		dp[2][i] = max(dp[0][i - 1], dp[1][i - 1]);
	}

	cout << max(dp[0][n], max(dp[1][n], dp[2][n])) << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	
	int t;

	cin >> t;

	while (t--) 
		solve();
	
	return 0;
}