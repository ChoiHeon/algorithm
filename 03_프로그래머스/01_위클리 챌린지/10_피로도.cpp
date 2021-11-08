// https://programmers.co.kr/learn/courses/30/lessons/87946

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int answer;

void travel(int m, int x, const vector<vector<int>>& dungeons, int visited) {
	bool finish = true;

	for (int i = 0; i < n; i++) {
		if (!(visited & (1 << i)) && m >= dungeons[i][0]) {
			finish = false;
			travel(m - dungeons[i][1], x + 1, dungeons, visited | (1 << i));
		}
	}

	if (finish)
		answer = max(answer, x);
}

int solution(int k, vector<vector<int>> dungeons) {
	n = dungeons.size();
	answer = 0;

	for (int i = 0; i < n; i++) {
		if (k >= dungeons[i][0])
			travel(k - dungeons[i][1], 1, dungeons, 1 << i);
	}

	return answer;
}


int main() {


	return 0;
}