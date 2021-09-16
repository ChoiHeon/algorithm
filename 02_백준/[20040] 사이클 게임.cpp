// 문제: https://www.acmicpc.net/problem/20040

#include <iostream>
#include <stack>

using namespace std;

int n, m;
int answer;
int parent[500000];

void init() {
	for (int i = 0; i < n; i++)
		parent[i] = i;
}

int find(int x) {
	if (x == parent[x])
		return x;
	return parent[x] = find(parent[x]);
}

void merge(int x, int y) {
	x = find(x);
	y = find(y);
	if (x < y)	parent[y] = x;
	else		parent[x] = y;
}

void solve() {
	int v, u;

	for (int i = 0; i < m; i++) {
		cin >> v >> u;

		if (find(v) == find(u)) {
			answer = i + 1;
			break;
		}

		merge(v, u);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	cin >> n >> m;
	answer = 0;
	init();

	solve();

	cout << answer << endl;

	return 0;
}