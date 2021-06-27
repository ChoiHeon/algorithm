#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int INF = 987654321;
int T, N, K, M, L;
int lecture[12];
int semester[10];
int cache[10][1 << 12];

int bitCount(int n) {
	int ret = 0;
	
	for (int i = 0; i < 12; i++)
		if (n & (1 << i))
			ret += 1;

	return ret;
}

int solution(int answer, int taken)
{
	//K개 이상의 과목을 이미 들은 경우
	if (bitCount(taken) >= K) return 0;

	//M학기가 지난 경우
	if (answer == M) return INF;

	int& res = cache[answer][taken];
	if (res != -1) return res;
	res = INF;

	//이번학기에 들을 수 있는 과목과 아직 안들은 과목
	int canTake = (semester[answer] & ~taken);

	//아직 선수과목을 다 듣지 않은 과목은 제외
	for (int i = 0; i < N; i++) {
		if ((canTake & (1 << i)) && (taken & lecture[i]) != lecture[i])
			canTake &= ~(1 << i);
	}

	//모든 부분집합 중에서 L개 이하의 과목을 듣는경우 다음 학기로 넘어간다.
	for (int take = canTake; take > 0; take = ((take - 1) & canTake)) {
		if (bitCount(take) > L) continue;
		res = min(res, solution(answer + 1, taken | take) + 1);
	}

	//이번학기를 건너뛰는 경우
	res = min(res, solution(answer + 1, taken));
	return res;
}

int main() {
	
	cin >> T;

	while (T--) {
		cin >> N >> K >> M >> L;
		memset(lecture, 0, sizeof(lecture));
		memset(semester, 0, sizeof(semester));
		memset(cache, -1, sizeof(cache));

		for (int R, i = 0; i < N; i++) {
			cin >> R;

			for (int pre_lec, j = 0; j < R; j++) {
				cin >> pre_lec;
				lecture[i] |= pre_lec;
			}
		}

		for (int C, i = 0; i < M; i++) {
			cin >> C;

			for (int num, j = 0; j < C; j++) {
				cin >> num;
				semester[i] |= num;
			}
		}

		int result = solution(0, 0);

		if (result != INF)	cout << result << endl;
		else				cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}