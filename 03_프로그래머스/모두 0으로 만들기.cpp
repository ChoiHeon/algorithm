// https://programmers.co.kr/learn/courses/30/lessons/77885

#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <cstdlib>

using namespace std;


long long dfs(vector<long long>& b, vector<vector<int>>& graph, int crnt, int prev) {
	long long ret = 0LL;

	for (auto next : graph[crnt]) {
		if (next == prev)
			continue;
		ret += dfs(b, graph, next, crnt);
	}

	b[prev] += b[crnt];
	ret += abs(b[crnt]);

	return ret;
}

long long solution(vector<int> a, vector<vector<int>> edges) {
	long long answer;
	vector<vector<int>> graph(a.size());
	vector<long long> b(a.size());

	for (int i = 0; i < a.size(); i++)
		b[i] = a[i];

	for (auto edge : edges) {
		graph[edge[0]].push_back(edge[1]);
		graph[edge[1]].push_back(edge[0]);
	}

	answer = dfs(b, graph, 0, 0);

	return b[0] == 0 ? answer : -1;
}


int main() {
	long long a = 0LL;
	a += 1000000000000000;

	cout << a;
}