// https://programmers.co.kr/learn/courses/30/lessons/86971


#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int childCnt[101]; // include self
vector<vector<int>> edges;

void init(int prev, int crnt) {
	childCnt[crnt] = 1;

	for (int next : edges[crnt]) {
		if (next == prev)
			continue;

		init(crnt, next);
		childCnt[crnt] += childCnt[next];
	}
}

int solution(int n, vector<vector<int>> wires) {
	int answer = n;

	edges.resize(n + 1);

	for (auto& w : wires) {
		edges[w[0]].push_back(w[1]);
		edges[w[1]].push_back(w[0]);
	}

	init(0, 1);
	
	for (int v = 2; v <= n; ++v) {
		int diff = abs(n - childCnt[v] - childCnt[v]);

		if (diff < answer)
			answer = diff;
	}

	return answer;
}

int main() {

	

	return 0;
}