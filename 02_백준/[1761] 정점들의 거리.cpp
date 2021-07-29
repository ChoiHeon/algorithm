// 문제: https://www.acmicpc.net/problem/1761

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int MAX_N = 400001;
const int LOG_N = 20;

int n, m;
int dist[MAX_N];
int depth[MAX_N];
int parent[MAX_N][LOG_N];
vector<vector<pair<int, int>>> info;

void Initialize(int prev, int current) {
	depth[current] = depth[prev] + 1;
	parent[current][0] = prev;

	for (auto e : info[current]) {
		if (e.first == prev)
			continue;

		dist[e.first] = dist[current] + e.second;
		Initialize(current, e.first);
	}
}

void DP() {

	for (int k = 0; k < LOG_N - 1; k++)
		for (int u = 1; u <= n; u++)
			if (parent[u][k] != -1)
				parent[u][k + 1] = parent[parent[u][k]][k];
}

// Lower Common Ancestor
int LCA(int u, int v) {	
	if (depth[u] < depth[v])	// u의 깊이가 더 크도록 교환
		swap(u, v);

	int k = 0;
	int diff = depth[u] - depth[v];

	while (diff) {				// u의 깊이가 v와 같도록 조상 노드로 이동
		if (diff % 2)
			u = parent[u][k];

		k++;
		diff /= 2;
	}

	if (u != v) {							// 깊이가 같은 u와 v가 다를 경우
		for (k = LOG_N - 1; k >= 0; k--)	// 가장 위의 노드부터 같을 때까지 탐색
			if (parent[u][k] != -1 && parent[u][k] != parent[v][k]) {
				u = parent[u][k];
				v = parent[v][k];
			}
	
		u = parent[u][0]; //  parent[u][0] == parent[v][0]
	}

	return u;
}

int main() {
	int a, b, c;
	int ret;

	scanf("%d", &n);

	memset(parent, -1, sizeof(parent));
	info.assign(n + 1, vector<pair<int, int>>());

	for (int i = 0; i < n - 1; i++) {
		scanf("%d %d %d", &a, &b, &c);

		info[a].push_back({ b, c });
		info[b].push_back({ a, c });
	}
	
	dist[1] = 0;
	depth[0] = -1;
	Initialize(0, 1);

	DP();

	scanf("%d", &m);

	while(m--) {
		scanf("%d %d", &a, &b);

		c = LCA(a, b);
		ret = dist[a] + dist[b] - 2 * dist[c];

		printf("%d\n", ret);
	}

	return 0;
}