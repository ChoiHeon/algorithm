// https://www.acmicpc.net/problem/4386

#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> pii;
typedef pair<float, float> pff;


int n;
int parents[100];
vector<pff> stars;
vector<pair<float, pii>> dists;

inline float distance(const pff& a, const pff& b) {
	return powf(a.first - b.first, 2) + powf(a.second - b.second, 2);
}

int find(int x) {
	if (x == parents[x])
		return x;
	return parents[x] = find(parents[x]);
}

void merge(int x, int y) {
	x = find(x);
	y = find(y);
	if (x < y)	parents[y] = x;
	else		parents[x] = y;;
}

int main() {
	
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		float x, y;
		scanf("%f %f", &x, &y);
		stars.push_back({ x, y });
		parents[i] = i;
	}

	for (int i = 0; i < n - 1; i++)
		for (int j = i + 1; j < n; j++)
			dists.push_back({ distance(stars[i], stars[j]), {i, j} });
		
	sort(dists.begin(), dists.end(), [](auto& a, auto& b)-> bool { return a.first < b.first; });

	float answer = 0;

	for (auto e : dists) {
		float d = e.first;
		int x = e.second.first;
		int y = e.second.second;

		if (find(x) != find(y)) {
			answer += sqrtf(d);
			merge(x, y);
		}
	}

	printf("%.2f", answer);

	return 0;
}
