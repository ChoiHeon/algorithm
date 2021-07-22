// https://www.acmicpc.net/problem/2568

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
typedef pair<int, int> pii;


int n;
int parents[100000];
vector<pii> X;
vector<pii> Y;
vector<pii> Z;
vector<pair<int, pii>> info;

int find(int x) {
	if (x == parents[x])
		return x;
	return parents[x] = find(parents[x]);
}

void merge(int x, int y) {
	x = find(x); y = find(y);
	if (x < y)
		parents[y] = x;
	else
		parents[x] = y;
}

int main() {

	scanf("%d", &n);
	for (int x, y, z, i = 0; i < n; i++) {
		scanf("%d %d %d", &x, &y, &z);
		parents[i] = i;
		X.push_back({ x, i });
		Y.push_back({ y, i });
		Z.push_back({ z, i });
	}

	sort(X.begin(), X.end());
	sort(Y.begin(), Y.end());
	sort(Z.begin(), Z.end());

	for (int i = 0; i < n - 1; i++) {
		info.push_back({ X[i + 1].first - X[i].first, {X[i + 1].second, X[i].second} });
		info.push_back({ Y[i + 1].first - Y[i].first, {Y[i + 1].second, Y[i].second} });
		info.push_back({ Z[i + 1].first - Z[i].first, {Z[i + 1].second, Z[i].second} });
	}

	sort(info.begin(), info.end());

	int answer = 0;
	for (auto e : info) {
		int a = e.second.first;
		int b = e.second.second;

		if (find(a) != find(b)) {
			merge(a, b);
			answer += e.first;
		}
	}

	printf("%d\n", answer);

	return 0;
}
