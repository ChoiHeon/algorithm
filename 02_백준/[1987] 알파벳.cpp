// https://www.acmicpc.net/problem/1799

#include <iostream>
#include <string>
#include <tuple>
#include <queue>

using namespace std;
typedef tuple<int, int, int> tiii;

inline int ctob(char c) { return (1 << (c - 'A')); }

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int r, c;
	int answer = 0;
	string board[20];

	cin >> r >> c;

	for (int i = 0; i < r; ++i)
		cin >> board[i];

	int dir_x[4] = { 0, 0, 1, -1 };
	int dir_y[4] = { 1, -1, 0, 0 };
	queue<tiii> q;

	q.push(make_tuple(1, 0, ctob(board[0][0])));	// (count, pos, path)

	while (q.size() > 0) {
		tiii ele = q.front();
		q.pop();

		int count = get<0>(ele);
		int x = get<1>(ele) / c;
		int y = get<1>(ele) % c;
		int path = get<2>(ele);
		
		answer = max(answer, count);

		for (int i = 0; i < 4; ++i) {
			int n_x = x + dir_x[i];
			int n_y = y + dir_y[i];

			if (n_x < 0 || n_x >= r || n_y < 0 || n_y >= c)	continue;
			if (path & ctob(board[n_x][n_y]))				continue;

			q.push(make_tuple(count + 1, n_x * c + n_y, path | ctob(board[n_x][n_y])));
		}
	}

	cout << answer << endl;

	return 0;
}