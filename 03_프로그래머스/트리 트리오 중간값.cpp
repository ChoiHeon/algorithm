// https://programmers.co.kr/learn/courses/30/lessons/68937

#include <regex>
#include <iostream>

#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;
typedef pair<int, int> pii;

int n;
vector<vector<int>> graph;
vector<int> dist;


int bfs(int s) {
	deque<pii> queue;
	vector<bool> visited(n, false);
	int farthest = 0;

	queue.push_back({ s, 0 });
	dist.clear();

	while (queue.size() > 0) {
		pii element = queue.front();
		queue.pop_front();

		if (farthest < element.second) {
			farthest = element.second;
			dist.clear();
			dist.push_back(element.first);
		}
		else if (farthest == element.second)
			dist.push_back(element.first);

		for (auto next : graph[element.first]) {
			if (visited[next] == false) {
				visited[next] = true;
				queue.push_back({ next, element.second + 1 });
			}
		}
	}

	return farthest;
}

int solution(int num, vector<vector<int>> edges) {
	n = num;
	int farthest;

	graph.resize(n, vector<int>());

	for (auto &edge : edges) {
		graph[edge[0] - 1].push_back(edge[1] - 1);
		graph[edge[1] - 1].push_back(edge[0] - 1);
	}


	bfs(0);
	farthest = bfs(dist[0]);

	if (dist.size() > 1)
		return farthest;

	bfs(dist[0]);

	if (dist.size() > 1)
		return farthest;

	return farthest - 1;
}



int main() {
	int a = 4;
	vector<vector<int>> b{ {1, 2}, {2, 3}, {3, 4} };

	cout << solution(a, b) << endl;
}
