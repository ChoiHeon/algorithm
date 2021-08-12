// 문제: https://www.acmicpc.net/problem/14267

#include <iostream>
#include <memory.h>
#include <vector>

using namespace std;

int n, m;
int answer[100000];
vector<vector<int>> junior;


void solve(int i, int w) {
	answer[i] += w;

	for (int j : junior[i])
		solve(j, answer[i]);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> n >> m;

	memset(answer, 0, sizeof(answer));
	junior.assign(n, vector<int>());

	int i, w;
	cin >> i;

	for (int j = 1; j < n; j++) {
		cin >> i;
		junior[--i].push_back(j);
	}

	while (m--) {
		cin >> i >> w;
		answer[--i] += w;
	}

	solve(0, 0);

	for (i = 0; i < n; i++)
		cout << answer[i] << " ";
	cout << "\n";

	return 0;
}