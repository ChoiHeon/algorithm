// https://www.acmicpc.net/problem/1647


#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>

using namespace std;
#define T(a, b, c) make_tuple(a, b, c)
typedef tuple<int, int, int> tiii;

int parents[100001];
vector<tiii> edges;

int _find(int x) {
	if (x == parents[x])
		return x;
	return parents[x] = _find(parents[x]);
}

void _union(int x, int y) {
	x = _find(x);
	y = _find(y);
	if (x < y)	parents[x] = y;
	else		parents[y] = x;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;
	int answer = 0;
	int del_edge = 0;

	cin >> n >> m;

	for (int i = 1; i <= n; i++)
		parents[i] = i;

	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		edges.push_back(T(a, b, c));
	}

	sort(edges.begin(), edges.end(),
		[](tiii a, tiii b) -> bool { return get<2>(a) < get<2>(b); }
	);

	for (auto edge : edges) {
		int v = get<0>(edge);
		int u = get<1>(edge);
		int c = get<2>(edge);

		if (_find(v) != _find(u)) {
			answer += c;
			del_edge = del_edge < c ? c : del_edge;
			_union(v, u);
		}
	}

	answer -= del_edge;
	cout << answer << endl;

	return 0;
}
