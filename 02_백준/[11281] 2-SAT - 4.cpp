// https://www.acmicpc.net/problem/11281

#include <iostream>
#include <memory.h>
#include <vector>
#include <stack>
#include <set>
#include <algorithm>


using namespace std;

const int MAX = 20002;

int id = 0;
int sid = 1;
int sccId[MAX];
int nodeId[MAX];
bool finished[MAX];
vector<int> edges[MAX];
stack<int> s;


int notX(int x)		{ return x ^ 1; }
int trueX(int x)	{ return x << 1; }
int falseX(int x)	{ return x << 1 | 1; }

int dfs(int x) {
	int parent = ++id;
	nodeId[x] = parent;
	s.push(x);

	for (int y : edges[x]) {
		if (nodeId[y] == -1)
			parent = min(parent, dfs(y));
		else if (!finished[y])
			parent = min(parent, nodeId[y]);
	}

	if (parent == nodeId[x]) {
		while (true) {
			int t = s.top();  s.pop();
			sccId[t] = sid;
			finished[t] = true;
			if (t == x)  break;
		}

		++sid;
	}

	return parent;
}

void two_SAT() {
	int n, m;
	cin >> n >> m;
	memset(nodeId, -1, sizeof(nodeId));
	memset(finished, 0, sizeof(finished));

	for (int i = 0; i < m; ++i) {
		int x, y;
		cin >> x >> y;

		x = x < 0 ? falseX(-x) : trueX(x);
		y = y < 0 ? falseX(-y) : trueX(y);

		edges[notX(x)].push_back(y);
		edges[notX(y)].push_back(x);
	}

	for (int x = 1; x <= n * 2 + 1; ++x) {
		if (nodeId[x] == -1)
			dfs(x);
	}

	for (int x = 1; x <= n; ++x) {
		int x1 = trueX(x);
		int x2 = falseX(x);

		if (sccId[x1] == sccId[x2]) {
			cout << "0" << endl;
			return;
		}
	}

	cout << "1\n";

	for (int x = 1; x <= n; ++x) {
		int x1 = trueX(x);
		int x2 = falseX(x);

		if (sccId[x1] < sccId[x2])
			cout << "1 ";
		else
			cout << "0 ";
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	two_SAT();

	return 0;
}