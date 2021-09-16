// problem: 2-SAT - 4
// link : https ://www.acmicpc.net/problem/11281

#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define rep(i,n) for(int i=0;i<n;++i)
#define REP(i,n) for(int i=1;i<=n;++i)
#define FAST cin.tie(NULL);cout.tie(NULL); ios::sync_with_stdio(false)
using namespace std;

#define t(x) (x<<1)
#define f(x) (x<<1|1)
#define W(x) (x>0?t(x-1):f(-(x+1)))

int N, M, u, v, order, id;

vector<vector<int>> adj;
vector<int> discovered, sccid;
stack<int> st;
void OR(int u, int v) {
	adj[W(u) ^ 1].emplace_back(W(v));
	adj[W(v) ^ 1].emplace_back(W(u));
}

int scc(int here) {
	int ret = discovered[here] = order++;
	st.emplace(here);
	for (auto there : adj[here]) {
		if (discovered[there] == -1) ret = min(ret, scc(there));
		else if (sccid[there] == -1) ret = min(ret, discovered[there]);
	}

	if (ret == discovered[here]) {
		while (1) {
			int t = st.top();
			st.pop();
			sccid[t] = id;
			if (t == here) break;
		}
		++id;
	}
	return ret;
}

int main() {
	FAST;

	cin >> N >> M;
	adj.resize(N << 1);
	rep(i, M) {
		cin >> u >> v;
		OR(u, v);
	}
	discovered = sccid = vector<int>(N << 1, -1);
	rep(i, N << 1) if (discovered[i] == -1) scc(i);

	bool flag = 1;

	rep(i, N) if (sccid[t(i)] == sccid[f(i)]) {
		flag = 0;
		break;
	}

	cout << flag << '\n';

	if (flag) {
		rep(i, N) {
			if (sccid[t(i)] < sccid[f(i)])
				cout << 1 << ' ';
			else
				cout << 0 << ' ';
		}
	}
	return 0;
}
