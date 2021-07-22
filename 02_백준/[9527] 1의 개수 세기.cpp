// https://www.acmicpc.net/problem/9527

#include <iostream>
#include <cmath>

using namespace std;

const int MAX = 55;
long long a, b;
long long cache[MAX];

int bit_count(long long x) {
	if (x == 0LL)
		return 0;
	return 1 + bit_count(x / 2);
}

long long solve(long long x) {
	int cnt = bit_count(x);
	long long y = x + 1;
	long long ret = 0LL;

	for (int i = 1; i <= cnt; i++) {
		ret += (y / cache[i]) * cache[i - 1];

		if (y % cache[i] > cache[i - 1])
			ret += (y % cache[i]) - cache[i - 1];
	}

	return ret;
}

int main() {

	// input data
	long long a, b;
	cin >> a >> b;

	// calculate cache
	cache[0] = 1LL;
	for (int i = 1; i < MAX; i++)
		cache[i] = cache[i - 1] + cache[i - 1];

	// solve
	long long ret = solve(b) - solve(a - 1);
	cout << ret << endl;

	return 0;
}


