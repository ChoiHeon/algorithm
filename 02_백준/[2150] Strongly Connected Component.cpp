// 문제: https://www.acmicpc.net/problem/2150

#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <stack>

using namespace std;

int n, m;
int order;
int num[10001];
int low[10001];
bool visited[10001];
stack<int> s;
vector<vector<int>> edge;
vector<vector<int>> answer;


void dfs_tree(int v) {
	if (visited[v]) return;
	
	visited[v] = true;
	num[v] = ++order;
	low[v] = order;
	s.push(v);

	for (int u : edge[v]) {
		if (!num[u]) {			// tree edge
			dfs_tree(u);
			low[v] = min(low[v], low[u]);
		}
		else if (visited[u])	// back edge
			low[v] = min(low[v], num[u]);
	}

	if (low[v] == num[v]) {
		vector<int> scc;

		while (!s.empty()) {
			int poped = s.top();
			s.pop();
			visited[poped] = false;
			scc.push_back(poped);

			if (poped == v) break;
		}

		sort(scc.begin(), scc.end());
		answer.push_back(scc);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> n >> m;

	memset(num, 0, sizeof(num));
	memset(low, 0, sizeof(num));
	memset(visited, false, sizeof(visited));
	edge.assign(n + 1, vector<int>());

	for (int i = 0; i < m; i++) {
		int v, u;
		cin >> v >> u;
		edge[v].push_back(u);
	}

	order = 0;

	for (int v = 1; v <= n; v++) {
		if (!num[v])	
			dfs_tree(v);
	}

	sort(answer.begin(), answer.end(),
		[](auto& a, auto& b)->bool { return a.front() < b.front(); });

	cout << answer.size() << "\n";
	
	for (auto scc : answer) {
		for (int v : scc)
			cout << v << " ";
		cout << "-1\n";
	}

	return 0;
}
