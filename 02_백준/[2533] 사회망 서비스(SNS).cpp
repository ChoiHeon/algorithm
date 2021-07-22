// https://www.acmicpc.net/problem/2533

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int n;
int dp[1000001][2];
vector<vector<int>> edges;

int solve (int prev, int crnt, int parent_state) {
	if (dp[crnt][parent_state])
		return dp[crnt][parent_state];

	int ret;

	if (parent_state) {
		int ret1 = 0 , ret2 = 1;
		for (int child : edges[crnt]) {
			if (child != prev) {
				ret1 += solve(crnt, child, 0);
				ret2 += solve(crnt, child, 1);
			}
		}
		ret = ret1 < ret2 ? ret1 : ret2;
	}
	else {
		ret = 1;
		for (int child : edges[crnt])
			if (child != prev)
				ret += solve(crnt, child, 1);
	}

	return dp[crnt][parent_state] = ret;
}

int main() {

	scanf("%d", &n);
	memset(dp, 0, sizeof(dp));
	edges.assign(n + 1, vector<int>());
	for (int v, u, i = 0; i < n - 1; i++) {
		scanf("%d %d", &v, &u);
		edges[v].push_back(u);
		edges[u].push_back(v);
	}

	int answer = solve(0, 1, true);
	printf("%d\n", answer);

	return 0;
}