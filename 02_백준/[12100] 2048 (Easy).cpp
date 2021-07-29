// a문제: https://www.acmicpc.net/problem/12100

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int n;
int answer;
int original[20][20];
vector<int> line;

inline int max(int a, int b) { return a < b ? b : a; }

void solve(int dir, int turn, const int (*board)[20]) {
	int ret[20][20];

	memset(ret, 0, sizeof(ret));

	switch (dir) {
	case 0: // left
		for (int i = 0; i < n; i++) {
			line.clear();

			for (int j = 0; j < n; j++) {
				if (board[i][j] == 0)
					continue;
				line.push_back(board[i][j]);
			}

			int p = 0, q = 0;
			while (q < line.size()) {
				if (q < line.size() - 1 && line[q] == line[q + 1]) {
					ret[i][p] = (line[q] << 1);
					q += 2;
				}
				else {
					ret[i][p] = line[q];
					q++;
				}
				p++;
			}
		}
		break;

	case 1: // right
		for (int i = 0; i < n; i++) {
			line.clear();

			for (int j = n - 1; j >= 0; j--) {
				if (board[i][j] == 0)
					continue;
				line.push_back(board[i][j]);
			}

			int p = n - 1, q = 0;
			while (q < line.size()) {
				if (q < line.size() - 1 && line[q] == line[q + 1]) {
					ret[i][p] = (line[q] << 1);
					q += 2;
				}
				else {
					ret[i][p] = line[q];
					q++;
				}
				p--;
			}
		}
		break;

	case 2: // up
		for (int j = 0; j < n; j++) {
			line.clear();
			
			for (int i = 0; i < n; i++) {
				if (board[i][j] == 0)
					continue;
				line.push_back(board[i][j]);
			}

			int p = 0, q = 0;
			while (q < line.size()) {
				if (q < line.size() - 1 && line[q] == line[q + 1]) {
					ret[p][j] = (line[q] << 1);
					q += 2;
				}
				else {
					ret[p][j] = line[q];
					q++;
				}
				p++;
			}
		}
		break;

	case 3: // down
		for (int j = 0; j < n; j++) {
			line.clear();

			for (int i = n - 1; i >= 0; i--) {
				if (board[i][j] == 0)
					continue;
				line.push_back(board[i][j]);
			}

			int p = n - 1, q = 0;
			while (q < line.size()) {
				if (q < line.size() - 1 && line[q] == line[q + 1]) {
					ret[p][j] = (line[q] << 1);
					q += 2;
				}
				else {
					ret[p][j] = line[q];
					q++;
				}
				p--;
			}
		}
		break;

	default:
		break;
	}

	if (turn == 5) {
		for (int i = 0; i < n; i++) 
			for (int j = 0; j < n; j++)
				if (answer < ret[i][j])
					answer = ret[i][j];
	}
	else {
		for (int i = 0; i < 4; i++)
			solve(i, turn + 1, ret);
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	cin >> n;
	answer = 0;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) 
			cin >> original[i][j];

	for (int i = 0; i < 4; i++)
		solve(i, 1, original);

	cout << answer << endl;
}