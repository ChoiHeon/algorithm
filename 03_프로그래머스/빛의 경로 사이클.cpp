// https://programmers.co.kr/learn/courses/30/lessons/86052

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


vector<int> solution(vector<string> grid) {
	typedef pair<int, int> PII;

	vector<int> answer;

	int n = grid.size();
	int m = grid[0].size();
	PII dirs[4] = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
	int L[4] = { 3, 0, 1, 2 };
	int R[4] = { 1, 2, 3, 0 };
	vector<pair<PII, int>> start_ray;	// { {시작 좌표}, {방향(index)} }
	vector<vector<vector<pair<int, int>>>> record;
	record.resize(n, vector<vector<PII>>(m, vector<PII>(4)));

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			for (int k = 0; k < 4; k++)
				start_ray.push_back({ { i, j }, k });

	for (int i = 0; i < start_ray.size(); ++i) {
		PII pos = start_ray[i].first;
		int dir_idx = start_ray[i].second;
		int cnt = 1;

		while (true) {
			if (record[pos.first][pos.second][dir_idx].second == 0) { // 방문한 기록이 없음
				record[pos.first][pos.second][dir_idx] = { i, cnt };

				if (grid[pos.first][pos.second] == 'R')			dir_idx = R[dir_idx];
				else if (grid[pos.first][pos.second] == 'L')	dir_idx = L[dir_idx];

				pos = { pos.first + dirs[dir_idx].first, pos.second + dirs[dir_idx].second };
				++cnt;

				if (pos.first == -1)		pos.first = n - 1;
				else if (pos.first == n)	pos.first = 0;
				else if (pos.second == -1)	pos.second = m - 1;
				else if (pos.second == m)	pos.second = 0;
			}
			else {
				if (record[pos.first][pos.second][dir_idx].first == i)  // 새로운 사이클 발견
					answer.push_back(cnt - record[pos.first][pos.second][dir_idx].second);

				break;
			}
		}
	}

	sort(answer.begin(), answer.end());

	return answer;
}

int main() {

	return 0;
}