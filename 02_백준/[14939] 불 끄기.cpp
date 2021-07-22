// https://www.acmicpc.net/problem/14939

#include <iostream>

using namespace std;

int org[10][10];
int cpy[10][10];
const int dir_x[4] = { 0, 0, -1, 1 };
const int dir_y[4] = { -1, 1, 0, 0 };

bool is_in_range(int x, int y) {
	return !(x < 0 || y < 0 || x > 9 || y > 9);
}

void turn(int x, int y) {
	for (int k = 0; k < 4; k++) {
		int n_x = x + dir_x[k];
		int n_y = y + dir_y[k];

		if (is_in_range(n_x, n_y))
			cpy[n_x][n_y] ^= 1;
	}

	cpy[x][y] ^= 1;
}

void copy() {
	for (int i = 0; i < 10; i++)
		for (int j = 0; j < 10; j++)
			cpy[i][j] = org[i][j];
}

bool is_dark() {
	for (int i = 0; i < 10; i++)
		for (int j = 0; j < 10; j++)
			if (cpy[i][j])
				return false;
	return true;
}

int main() {

	int ans = 0x7f7f7f7f;

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			char c;
			cin >> c;
			org[i][j] = c == '#' ? 0 : 1;
		}
	}
		
	for (int bm = 0; bm < (1 << 10); bm++) {
		int cnt = 0;

		copy(); // 초기 상태를 복사
		
		for (int y = 0; y < 10; y++) { // 첫 번째 줄에 대한 모든 경우의 수
			if (bm & (1 << y)) {
				turn(0, y);
				cnt++;
			}
		}

		for (int x = 1; x < 10; x++) { // 나머지 줄을 대해서 탐색
			for (int y = 0; y < 10; y++) {
				if (cpy[x - 1][y]) {
					turn(x, y);
					cnt++;
				}
			}
		}

		if (is_dark())
			ans = cnt < ans ? cnt : ans;
	}
	
	cout << ans << endl;

	return 0;
}


