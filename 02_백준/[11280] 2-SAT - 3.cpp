// https://www.acmicpc.net/problem/11280

#include <iostream>
#include <memory.h>
#include <vector>
#include <stack>
#include <set>
#include <algorithm>


using namespace std;

const int MAX = 20002;

int id = 1;
int nodeId[MAX];
bool finished[MAX];
vector<int> edges[MAX];
vector<set<int>> SCC;
stack<int> s;


int notX(int x)		{ return x ^ 1; }
int trueX(int x)	{ return x << 1; }
int falseX(int x)	{ return x << 1 | 1; }

int dfs(int x) {
	int parent = ++id;
	nodeId[x] = parent;
	s.push(x);

	for (int y : edges[x]) {
		if (nodeId[y] == 0)
			parent = min(parent, dfs(y));
		else if (!finished[y])
			parent = min(parent, nodeId[y]);
	}

	if (parent == nodeId[x]) {
		set<int> scc;
		
		while (true) {
			int t = s.top();  s.pop();
			scc.insert(t);
			finished[t] = true;
			if (t == x)  break;
		}

		SCC.push_back(scc);
	}

	return parent;
}

int two_SAT() {
	int n, m;
	cin >> n >> m;
	memset(nodeId, 0, sizeof(nodeId));
	memset(finished, 0, sizeof(finished));

	for (int i = 0; i < m; ++i) {
		int x, y;
		cin >> x >> y;

		x = x < 0 ? falseX(-x) : trueX(x);
		y = y < 0 ? falseX(-y) : trueX(y);

		edges[notX(x)].push_back(y);
		edges[notX(y)].push_back(x);
	}

	n *= 2;
	for (int x = 1; x <= n; ++x) {
		if (!nodeId[x])
			dfs(x);
	}

	bool valid = true;
	for (auto& scc : SCC) {
		auto end = scc.end();

		for (int x : scc) {
			if (scc.find(notX(x)) != end) {
				valid = false;
				break;
			}
		}

		if (!valid)  break;
	}

	return valid ? 1 : 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int answer = two_SAT();

	cout << answer << endl;

	return 0;
}