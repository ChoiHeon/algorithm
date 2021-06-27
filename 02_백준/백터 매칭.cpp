// https://www.acmicpc.net/problem/1007

#include <iostream>
#include <cmath>

using namespace std;

#define P(a, b) make_pair(a, b)
#define MIN(a, b) a < b ? a : b
#define SIZE(a) sqrt(a.first * a.first + a.second * a.second)
#define ADD(a, b) P(a.first + b.first, a.second + b.second)
#define SUB(a, b) P(a.first - b.first, a.second - b.second)

typedef long long ll;
typedef pair<ll, ll> pll;

int n;
pll p[20];
double answer;

void solve(int k, int cnt, pll v) {
	if (n == k) {
		answer = MIN(answer, SIZE(v));
		return;
	}

	int m = n / 2;

	if (cnt < m)
		solve(k + 1, cnt + 1, ADD(v, p[k]));
	if (m - cnt != n - k)
		solve(k + 1, cnt, SUB(v, p[k]));
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cout << fixed;
	cout.precision(6);

	int t;
	cin >> t;

	while (t--) {
		cin >> n;
		answer = 0x7f7f7f7f7f7f7f7f;

		for (int i = 0; i < n; i++)
			cin >> p[i].first >> p[i].second;

		solve(0, 0, P(0, 0));
		cout << answer << endl;
	}

	return 0;
}