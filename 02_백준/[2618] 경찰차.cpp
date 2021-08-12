// 문제: https://www.acmicpc.net/problem/2618

#include <iostream>
#include <memory.h>
#include <vector>

using namespace std;
typedef pair<int, int> pii;

int n, m;
int cache[1001][1001];
vector<pii> path_A;
vector<pii> path_B;

inline int min(int i, int j) { return i < j ? i : j; }
inline int max(int i, int j) { return i > j ? i : j; }

int getMinDistance(int a, int b) {
	if (a == m || b == m)
		return 0;

	int& ret = cache[a][b];

	if (ret != -1)
		return ret;

	ret = 0x7f7f7f7f;

	int max_location = max(a, b) + 1;
	int dist_A = abs(path_A[max_location].first - path_A[a].first) +
				 abs(path_A[max_location].second - path_A[a].second);
	int dist_B = abs(path_B[max_location].first - path_B[b].first) +
				 abs(path_B[max_location].second - path_B[b].second);
	int ret1 = getMinDistance(max_location, b) + dist_A;
	int ret2 = getMinDistance(a, max_location) + dist_B;

	ret = min(ret1, ret2);

	return ret;
}

void trackPath(int a, int b) {
	if (a == m || b == m)
		return;

	int max_location = max(a, b) + 1;
	int dist_A = abs(path_A[max_location].first - path_A[a].first) +
				 abs(path_A[max_location].second - path_A[a].second);
	int dist_B = abs(path_B[max_location].first - path_B[b].first) +
				 abs(path_B[max_location].second - path_B[b].second);
	int ret1 = getMinDistance(max_location, b) + dist_A;
	int ret2 = getMinDistance(a, max_location) + dist_B;

	if (ret1 > ret2) {
		printf("2\n");
		trackPath(a, max_location);
	}
	else {
		printf("1\n");
		trackPath(max_location, b);
	}
}

int main() {

	scanf("%d", &n);
	scanf("%d", &m);
	memset(cache, -1, sizeof(cache));

	path_A.push_back({ 1, 1 });
	path_B.push_back({ n, n });

	int x, y;

	for (int i = 0; i < m; i++) {
		scanf("%d %d", &x, &y);
		path_A.push_back({ x, y });
		path_B.push_back({ x, y });
	}

	printf("%d\n", getMinDistance(0, 0));
	trackPath(0, 0);

	return 0;
}
