#include <iostream>
#include <memory.h>
#include <set>
#include <queue>
#include <algorithm>
#include <unordered_map>

using namespace std;



int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n, m;
	int prev[32001];
	unordered_map<int, set<int>> next;
	priority_queue<int, vector<int>, greater<int>> p_queue;

	cin >> n >> m;
	memset(prev, 0, sizeof(prev));

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		prev[b]++;
		next[a].insert(b);
	}

	for (int i = 1; i <= n; i++) {
		if (prev[i] == 0) {
			p_queue.push(i);
		}
	}

	while (!p_queue.empty()) {
		int a = p_queue.top();
		p_queue.pop();

		cout << a << " ";

		for (int b : next[a]) {
			prev[b]--;
			if (prev[b] == 0)
				p_queue.push(b);
		}
	}
}
