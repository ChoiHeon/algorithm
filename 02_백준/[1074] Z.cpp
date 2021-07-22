// https://www.acmicpc.net/problem/9095


#include <iostream>
#include <cstring>


using namespace std;

typedef long long ll;

ll cache[17];

void init_cache() {
	memset(cache, 0, sizeof(cache));
	cache[0] = 1LL;

	for (int i = 1; i < 17; i++)
		cache[i] = cache[i - 1] * 2;
}


ll solution(int n, int r, int c) {
	if (n == 0)
		return 0LL;

	ll k = cache[n - 1];

	if (r < k) {
		if (c < k) 
			return solution(n - 1, r, c);
		else
			return (k * k) + solution(n - 1, r, c - k);
	}
	else {
		if (c < k) 
			return (k * k) * 2 + solution(n - 1, r - k, c);
		else 
			return (k * k) * 3 + solution(n - 1, r - k, c - k);
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	init_cache();

	int n, r, c;
	cin >> n >> r >> c;

	cout << solution(n, r, c) << endl;

	return 0;
}