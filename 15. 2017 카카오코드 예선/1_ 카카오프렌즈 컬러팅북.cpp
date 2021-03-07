// https://programmers.co.kr/learn/courses/30/lessons/1829


#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;
typedef pair<int, int> pii;
#define m_p(a, b) make_pair(a, b)

int DFS(int m, int n, vector<vector<int>>& picture, int i, int j, set<pii>& s) {
	vector<pii> v;
	int x, y;
	int color = picture[i][j];
	int area_size = 0;
	int dx[4] = { 1, -1, 0, 0 };
	int dy[4] = { 0, 0, 1, -1 };
	int dir[4] = { 0, 1, 2, 3 };

	v.push_back(m_p(i, j));
	s.insert(m_p(i, j));

	while (v.size() > 0) {
		pii pos = v.back();

		v.pop_back();
		area_size++;

		for (int d : dir) {
			x = pos.first + dx[d];
			y = pos.second + dy[d];

			if (x < 0 || x >= m || y < 0 || y >= n)
				continue;
			if (s.find(m_p(x, y)) != s.end())
				continue;
			if (picture[x][y] != color)
				continue;

			v.push_back(m_p(x, y));
			s.insert(m_p(x, y));
		}
	}

	return area_size;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
	vector<int> answer(2);
	int max_area_size = 0;
	int area_count = 0;
	set<pii> s;

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (picture[i][j] == 0)
				continue;
			if (s.find(m_p(i, j)) != s.end())
				continue;

			int area_size = DFS(m, n, picture, i, j, s);

			max_area_size = max_area_size > area_size ? max_area_size : area_size;
			area_count++;
		}
	}

	answer[0] = area_count;
	answer[1] = max_area_size;

	return answer;
}


// test
int main() {
}
