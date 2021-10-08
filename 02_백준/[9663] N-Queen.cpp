// https://www.acmicpc.net/problem/9663


#include <iostream>
#include <memory.h>
#include <cmath>

using namespace std;

int n;
int answer;
int row[15];

void n_queens(int level) {
	if (level == n) {
		++answer;
		return;
	}

	for (int j = 0; j < n; ++j) {
		bool flag = true;

		for (int i = 0; i < level; ++i) {
			if (row[i] == j || abs(row[i] - j) == level - i) {
				flag = false;
				break;
			}
		}

		if (flag) {
			row[level] = j;
			n_queens(level + 1);
		}
	}
}

int main() {
	
	scanf("%d", &n);
	answer = 0;
	memset(row, -1, sizeof(row));
	
	n_queens(0);

	printf("%d\n", answer);

	return 0;
}