// https://www.acmicpc.net/problem/9095


#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>


using namespace std;

int cache[11];

int solution(int n) {
	memset(cache, 0, sizeof(cache));

	cache[0] = 1;

	for (int i = 1; i <= n; i++) {
		for (int k = 1; k <= 3; k++) {
			if (i < k)
				break;
			cache[i] += cache[i - k];
		}
	}

	for (int j = 0; j <= n; j++)
		cout << cache[j] << ' ';
	cout << endl;

	return cache[n];
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t, n;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> n;
		cout << solution(n) << endl;
	}
	return 0;
}