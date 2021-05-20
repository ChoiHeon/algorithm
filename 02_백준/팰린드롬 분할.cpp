// https://www.acmicpc.net/problem/1509


#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

int cache[2501][2501];
int dp[2501];

int main() {

	string s;
	cin >> s;
	s.insert(0, " ");

	int n = s.length();

	for (int i = 1; i <= n; i++) 
		cache[i][i] = 1; 
	for (int i = 1; i < n; i++) 
		if (s[i] == s[i + 1]) 
			cache[i][i + 1] = 1;
	for (int i = 2; i < n; i++)
		for (int j = 1; j <= n - i; j++)
			if (s[j] == s[i + j] && cache[j + 1][j + i - 1]) 
				cache[j][j + i] = 1;

	for (int i = 1; i < n; i++) {
		dp[i] = 98765;

		for (int j = 1; j <= i; j++)
			if (cache[j][i])
				dp[i] = min(dp[i], dp[j - 1] + 1);
	}

	cout << dp[n-1] << endl;

	return 0;
}