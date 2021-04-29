// https://www.acmicpc.net/problem/14719


#include <iostream>
#include <vector>

using namespace std;


int solution(int w, int h, vector<int>& board) {
	int result = 0;

	for (int i = 0; i <= h; i++) {
		int left = -1;
		int right = -1;

		for (int j = 0; j < w; j++) {
			if (board[j] < i)
				continue;

			if (left == -1)
				left = j;
			else
				right = j;

			if (right != -1) {
				result += (right - left - 1);
				left = right;
				right = -1;
			}
		}
	}

	return result;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int h, w;
	cin >> h >> w;

	vector<int> board(w);
	for (int i = 0; i < w; i++)
		cin >> board[i];

	cout << solution(w, h, board);
}