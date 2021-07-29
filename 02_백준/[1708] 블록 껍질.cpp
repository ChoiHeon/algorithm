// a문제: https://www.acmicpc.net/problem/1708

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

int n;
int answer;

ll ccw(pii a, pii b, pii c) {
	ll x1 = a.first, y1 = a.second;
	ll x2 = b.first, y2 = b.second;
	ll x3 = c.first, y3 = c.second;

	return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3;
}

void findConvex(pii& a, pii& b, vector<pii> &v) {
	ll dist = 0LL;
	pii d;
	vector<pii> u;

	for (auto& c : v) {
		ll tmp = ccw(a, b, c);
		if (tmp > 0LL) {
			u.push_back(c);
			if (tmp > dist) {
				dist = tmp;
				d = c;
			}
		}
	}

	if (!u.empty()) {
		answer++;
		findConvex(a, d, u);
		findConvex(d, b, u);
	}
}

int main() {

	scanf("%d", &n);
	
	vector<pii> points(n);

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &points[i].first, &points[i].second);
	}

	sort(points.begin(), points.end());

	pii a = points.front();
	pii b = points.back();
	
	answer = 2;
	findConvex(a, b, points);
	findConvex(b, a, points);

	printf("%d\n", answer);

	return 0;
}