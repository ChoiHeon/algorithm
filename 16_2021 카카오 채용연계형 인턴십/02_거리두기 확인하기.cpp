// 문제명: 거리두기 확인하기
// 링크: https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;


inline int manhattan(const pair<int, int>& p1, const pair<int, int>& p2) {
	return abs(p1.first - p2.first) + abs(p1.second - p2.second);
}

int follow(const vector<string>& place) {
	vector<pair<int, int>> p;

	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 5; j++)
			if (place[i][j] == 'P')
				p.push_back({ i, j });

	int m = p.size();

	for (int i = 0; i < m - 1; i++)
		for (int j = i + 1; j < m; j++) {

			int distance = manhattan(p[i], p[j]);

			if (distance == 1) {
				return 0;
			}
			else if (distance == 2) {
				if (p[i].first == p[j].first) {
					if (place[p[i].first][p[i].second + 1] != 'X')
						return 0;
				}
				else if (p[i].second == p[j].second) {
					if (place[p[i].first + 1][p[i].second] != 'X')
						return 0;
				}
				else {
					pair<int, int> q, r;

					if (p[i].second < p[j].second) {
						q = { p[i].first, p[i].second + 1 };
						r = { p[i].first + 1, p[i].second };
					}
					else {
						q = { p[j].first - 1, p[j].second };
						r = { p[j].first, p[j].second + 1 };
					}

					if (place[q.first][q.second] != 'X' || place[r.first][r.second] != 'X')
						return 0;
				}
			}
		}

	return 1;
}

vector<int> solution(vector<vector<string>> places) {
	vector<int> answer;
	answer.reserve(5);

	for (auto&& place : places)
		answer.push_back(follow(place));

	return answer;
}

int main() {

	int a = 10;
	const int& b = a;
	int& const c = a;
	cout << b << endl;

	c = 3;

	return 0;
}