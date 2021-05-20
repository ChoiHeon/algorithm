// https://programmers.co.kr/learn/courses/30/lessons/1832

#include <iostream>
#include <vector>
#include <set>

using namespace std;

#define P(a, b) make_pair(a, b)
typedef pair<int, int> pii;


int solution(int n, int m, vector<vector<int>>& board) {
	int answer = 0;
	int dirs[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
	vector<pii> outer;
	vector<pii> stack;
	vector<pii> melt;
	set<pii> cheeze;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (board[i][j] == 1)
				cheeze.insert(P(i, j));
		}
	}

	while (!cheeze.empty()) {
		outer.clear();
		stack.clear();
		stack.push_back(P(0, 0));

		while (!stack.empty()) {
			int x = stack.back().first;
			int y = stack.back().second;
			stack.pop_back();

			for (int i = 0; i < 4; i++) {
				int nx = x + dirs[i][0];
				int ny = y + dirs[i][1];

				if (nx < 0 || nx >= n || ny < 0 || ny >= m)
					continue;
				if (board[nx][ny] == 0)
					stack.push_back(P(nx, ny));
			}

			board[x][y] = -1;
			outer.push_back(P(x, y));
		}

		for (auto p : cheeze) {
			int i = p.first;
			int j = p.second;
			int adj = 0;

			if (board[i][j] != 1)
				continue;

			if (board[i - 1][j] == -1)	adj += 1;
			if (board[i][j - 1] == -1)	adj += 1;
			if (board[i + 1][j] == -1)	adj += 1;
			if (board[i][j + 1] == -1)	adj += 1;

			if (adj >= 2)
				melt.push_back(P(i, j));
			}


		for (auto p : melt) {
			cheeze.erase(p);
			board[p.first][p.second] = 0;
		}

		for (auto p : outer) {
			board[p.first][p.second] = 0;
		}
	
		answer += 1;
	}

	return answer;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, m = 0;
	vector<vector<int>> board;

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		board.push_back(vector<int>(m));
		for (int j = 0; j < m; j++)
			cin >> board[i][j];
	}

	cout << solution(n, m, board);
	
	return 0;
}