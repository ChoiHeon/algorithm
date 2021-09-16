// 문제: https://www.acmicpc.net/problem/3176

#include <iostream>
#include <memory.h>
#include <vector>
#include <map>
using namespace std;

const int MAX_NODE = 100001;
const int MAX_DEPTH = 17;

int n;
int depth[MAX_NODE];
int parent[MAX_NODE][MAX_DEPTH];	// parent[v][k] = v에서 2^k만큼 위에 있는 조상노드
									// parent[v][0] = v의 부모노드
									// parent[v][k+1] = parent[parent[v][k]][k]

int max_dist[MAX_NODE][MAX_DEPTH];	// max_dist[v][k] = v부터 v의 2^k만큼 위에 있는 조상노드까지의 최대 거리
									// max_dist[v][0] = v와 v의 부모와의 거리
									// max_dist[v][k+1] = max(max_dist[v][k], max_dist[parent[v][k]][k])

int min_dist[MAX_NODE][MAX_DEPTH];	// max_dist의 변형, 같은 점화식을 사용
vector<vector<int>> tree;
map<pair<int, int>, int> dist;

inline int max(int& a, int& b) { return a > b ? a : b; }
inline int min(int& a, int& b) { return a < b ? a : b; }

void init1(int prev, int crnt) {
	depth[crnt] = depth[prev] + 1;

	for (int child : tree[crnt]) {
		if (child == prev)
			continue;

		parent[child][0] = crnt;
		min_dist[child][0] = dist[{child, crnt}];
		max_dist[child][0] = min_dist[child][0];

		init1(crnt, child);
	}
}

void init2() {
	for (int k = 0; k < MAX_DEPTH - 1; k++)
		for (int v = 1; v <= n; v++)
			if (parent[v][k] != -1) {
				parent[v][k + 1] = parent[parent[v][k]][k];
				max_dist[v][k + 1] = max(max_dist[v][k], max_dist[parent[v][k]][k]);
				min_dist[v][k + 1] = min(min_dist[v][k], min_dist[parent[v][k]][k]);
			}
}

void search(int v, int u, int& max_d, int& min_d) {
	if (depth[v] > depth[u])
		swap(v, u);

	int diff = depth[u] - depth[v];

	for (int k = 0; diff; k++) {
		if (diff % 2) {
			max_d = max(max_d, max_dist[u][k]);
			min_d = min(min_d, min_dist[u][k]);

			u = parent[u][k];
		}

		diff /= 2;
	}

	if (v != u) {
		for (int k = MAX_DEPTH - 1; k >= 0; k--)
			if (parent[v][k] != -1 && parent[v][k] != parent[u][k]) {
				max_d = max(max_d, max_dist[v][k]);
				min_d = min(min_d, min_dist[v][k]);

				max_d = max(max_d, max_dist[u][k]);
				min_d = min(min_d, min_dist[u][k]);

				v = parent[v][k];
				u = parent[u][k];
			}

		max_d = max(max_d, max_dist[v][0]);
		min_d = min(min_d, min_dist[v][0]);

		max_d = max(max_d, max_dist[u][0]);
		min_d = min(min_d, min_dist[u][0]);
	}
}

void solve() {
	int m;
	int a, b;
	int max_d, min_d;

	cin >> m;

	while (m--) {
		cin >> a >> b;
		max_d = 0;
		min_d = 1000001;

		search(a, b, max_d, min_d);

		cout << min_d << " " << max_d << "\n";
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	
	cin >> n;
	depth[0] = -1;
	memset(parent, -1, sizeof(parent));
	tree.assign(n + 1, vector<int>());

	for (int i = 1; i < n; i++) {
		int v, u, c;
		cin >> v >> u >> c;

		tree[v].push_back(u);
		tree[u].push_back(v);

		dist[{v, u}] = c;
		dist[{u, v}] = c;
	}

	init1(0, 1);
	init2();

	solve();

	return 0;
}