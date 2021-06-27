#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

#define P(a, b) make_pair(a, b)
typedef pair<int, int> pii;

int n;
vector<vector<pii>> tree(10001);
int dist[10001];

void dijskstra(int start) {
	if (n == 1)
		return 0;

	vector<pii> heap;
	
	memset(dist, 0x3f, sizeof(dist));
	dist[start] = 0;
	heap.push_back(P(0, start));

	while (heap.size() > 0) {
		pii tmp = heap.back();
		int c = tmp.first;
		int v = tmp.second;
		heap.pop_back();

		if (dist[v] < c)
			continue;

		int u, d;
		for (pii next : tree[v]) {
			u = next.first;
			d = next.second;

			if (c + d < dist[u]) {
				dist[u] = c + d;
				heap.push_back(P(dist[u], u));
				push_heap(heap.begin(), heap.end(), greater<pii>());
			}
		}
	}
}

int solution() {
	int v = 0;
	int max_dist;

	dijskstra(1);
	max_dist = 0;
	for (int i = 1; i <= n; i++) {
		if (dist[i] > max_dist) {
			max_dist = dist[i];
			v = i;
		}
	}

	dijskstra(v);
	max_dist = 0;
	for (int i = 1; i <= n; i++)
		max_dist = max(max_dist, dist[i]);

	return max_dist;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n;

	int v, u, c;

	for (int i = 0; i < n-1; i++) {
		cin >> v >> u >> c;
		tree[v].push_back(P(u, c));
		tree[u].push_back(P(v, c));
	}

	int answer = solution();
	cout << answer << endl;

	return 0;
}