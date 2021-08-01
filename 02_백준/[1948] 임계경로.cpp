// 문제: https://www.acmicpc.net/problem/1948

#include <iostream>
#include <memory.h>
#include <vector>

using namespace std;

int n, m;
int s, e;
int road_cnt;
int dist[10001];
bool visited[10001];
vector<vector<int>> path;
vector<vector<pair<int, int>>> graph;

void searchPath(int prev, int crnt, int d) {
	if (d < dist[crnt])
		return;
	if (d != 0 && d == dist[crnt]) {
		path[crnt].emplace_back(prev);
		return;
	}

	dist[crnt] = d;
	path[crnt].clear();
	path[crnt].emplace_back(prev);

	for (auto& info : graph[crnt]) {
		int next = info.first;
		int c = info.second;

		searchPath(crnt, next, c + d);
	}
}

void trackPath(int v) {
	visited[v] = true;

	for (int u : path[v]) {
		road_cnt++;

		if (!visited[u])
			trackPath(u);
	}
}

int main() {
	scanf("%d", &n);
	scanf("%d", &m);

	memset(dist, 0, sizeof(dist));
	memset(visited, false, sizeof(visited));

	path.assign(n + 1, vector<int>());
	graph.assign(n + 1, vector<pair<int, int>>());

	for (int v, u, c, i = 0; i < m; i++) {
		scanf("%d %d %d", &v, &u, &c);
		graph[v].push_back({ u, c });
	}

	scanf("%d %d", &s, &e);

	road_cnt = -1;

	searchPath(0, s, 0);
	trackPath(e);

	printf("%d\n", dist[e]);
	printf("%d\n", road_cnt);

	return 0;
}