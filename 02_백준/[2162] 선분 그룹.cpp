// https://www.acmicpc.net/problem/2162

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
typedef pair<int, int> pii;
typedef pair<pii, pii> ppp;


int find(int* parents, int x) {
	if (parents[x] == x)
		return x;

	return parents[x] = find(parents, parents[x]);
}

void merge(int* parents, int x, int y) {
	x = find(parents, x);
	y = find(parents, y);

	if (x < y)	parents[y] = x;
	else		parents[x] = y;
}

int ccw(const pii& a, const pii& b, const pii& c) {
	int x1 = a.first, y1 = a.second;
	int x2 = b.first, y2 = b.second;
	int x3 = c.first, y3 = c.second;
	int f = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3);
	
	if (f > 0)	return 1;
	if (f < 0)	return -1;
	return 0;
}

bool is_cress(const ppp& A, const ppp& B) {
	pii a = A.first;
	pii b = A.second;
	pii c = B.first;
	pii d = B.second;

	int f1 = ccw(a, b, c) * ccw(a, b, d);
	int f2 = ccw(c, d, a) * ccw(c, d, b);

	if (f1 == 0 && f2 == 0)
	{
		if (a > b) swap(a, b);
		if (c > d) swap(c, d);

		return a <= d && c <= b;
	}
	return f1 <= 0 && f2 <= 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	int parents[3000];
	int max_count;
	vector<ppp> lines;
	unordered_map<int, int> counter;

	cin >> n;
	lines.reserve(n);

	for (int i = 0; i < n; i++) 
		parents[i] = i;

	for (int i = 0; i < n; i++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		lines.push_back({ { x1, y1 }, { x2, y2 } });
	}

	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			if (is_cress(lines[i], lines[j]))
				merge(parents, i, j);

	max_count = 0;

	for (int i = 0; i < n; i++)
		counter[find(parents, i)]++;

	for (auto p : counter)
		max_count = max_count < p.second ? p.second : max_count;

	cout << counter.size() << endl;
	cout << max_count << endl;

	return 0;
}
