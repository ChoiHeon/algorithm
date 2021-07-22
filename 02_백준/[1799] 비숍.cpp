// https://www.acmicpc.net/problem/1799

#include <iostream>
#include <memory.h>

using namespace std;

const int MAX = 10;
bool chess[MAX][MAX];		// 체스판의 상태
bool visited_1[MAX * 2];	// 우상 -> 좌하 대각선
bool visited_2[MAX * 2];	// 좌상 -> 우하 대각선
int bishop[2];				// 색에 따른 비숍의 최대 개수
int chess_size;				// 사용자가 입력한 체스판의 크기

void dfs(int cnt, int x, int y, int color) {
	if (x >= chess_size) {	// 다음 줄로 이동
		x = x % 2 == 0 ? 1 : 0;
		y++;
	}
	if (y >= chess_size) {			// 체스판 전체를 탐색했을 때,
		if (cnt > bishop[color])	// 최대 값 갱신 여부 확인
			bishop[color] = cnt;
		return;
	}

	if (chess[y][x] &&
		!visited_1[x + y] &&
		!visited_2[x - y + chess_size]) {

		visited_1[x + y] = true;
		visited_2[x - y + chess_size] = true;

		dfs(cnt + 1, x + 2, y, color);

		visited_1[x + y] = false;
		visited_2[x - y + chess_size] = false;
	}

	dfs(cnt, x + 2, y, color);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> chess_size;
	memset(visited_1, 0, sizeof(visited_1));
	memset(visited_2, 0, sizeof(visited_2));

	for (int i = 0; i < chess_size; i++)
		for (int j = 0; j < chess_size; j++)
			cin >> chess[i][j];

	dfs(0, 0, 0, 0);
	dfs(0, 1, 0, 1);

	cout << bishop[0] + bishop[1] << endl;
}
