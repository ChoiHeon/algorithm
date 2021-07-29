// 문제: https://www.acmicpc.net/problem/11437

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int MAX_NODE = 50001;
const int MAX_DEPTH = 16;

int n, m;
int depth[MAX_NODE];
int parent[MAX_NODE][MAX_DEPTH];
vector<vector<int>> tree;

void init(int prev, int current) {
	depth[current] = depth[prev] + 1;

	for (int child : tree[current]) {
		if (child == prev)
			continue;

		parent[child][0] = current;
		init(current, child);
	}
}

void DP() {

	for (int k = 0; k < MAX_DEPTH - 1; k++)
		for (int v = 1; v <= n; v++)
			if (parent[v][k] != -1)
				parent[v][k + 1] = parent[parent[v][k]][k];
}

int LCA(int v, int u) {
	if (depth[v] > depth[u])
		swap(v, u);

	int diff = depth[u] - depth[v];

	for (int k = 0; diff; k++) {
		if (diff % 2)
			u = parent[u][k];
		diff /= 2;
	}

	if (v != u) {
		for (int k = MAX_DEPTH - 1; k >= 0; k--) {
			if (parent[v][k] != -1 && parent[v][k] != parent[u][k]) {
				v = parent[v][k];
				u = parent[u][k];
			}
		}

		v = parent[v][0];
	}

	return v;
}

int main() {
	
	int v, u;

	scanf("%d", &n);

	tree.assign(n + 1, vector<int>());

	for (int i = 0; i < n - 1; i++) {
		scanf("%d %d", &v, &u);
		tree[v].push_back(u);
		tree[u].push_back(v);
	}

	depth[0] = -1;
	memset(parent, -1, sizeof(parent));
	init(0, 1);
	DP();

	scanf("%d", &m);
	
	while (m--) {
		scanf("%d %d", &v, &u);
		printf("%d\n", LCA(v, u));
	}


	return 0;
}