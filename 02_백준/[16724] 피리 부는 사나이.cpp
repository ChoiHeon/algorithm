// https://www.acmicpc.net/problem/16724

#include <iostream>
#include <map>

using namespace std;

int n, m;
char board[1000][1000];
int group[1000][1000];
map<char, pair<int, int>> dir = { {'D', {1, 0}}, {'U', {-1, 0}}, {'R', {0, 1}}, {'L', {0, -1}} };

int grouping(int x, int y, int num) {
	int n_x = x + dir[board[x][y]].first;
	int n_y = y + dir[board[x][y]].second;
	
	group[x][y] = num;

	if (group[n_x][n_y])
		return group[x][y] = group[n_x][n_y];

	return group[x][y] = grouping(n_x, n_y, num);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n >> m;

	for (int i = 0; i < n; i++) 
		for (int j = 0; j < m; j++) {
			cin >> board[i][j];
			group[i][j] = 0;
		}

	int answer = 0;
	int group_num = 1;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			if (group[i][j])
				continue;

			grouping(i, j, group_num);

			if (group[i][j] == group_num)
				answer++;

			group_num++;
		}

	cout << answer << endl;
	
	return 0;
}