// 문제: https://programmers.co.kr/learn/courses/30/lessons/42862

#include <regex>
#include <iostream>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	vector<int> v(1, n);
	int answer = 0;

	for (int i : lost)		v[i + 1]--;
	for (int i : reserve)	v[i + 1]++;

	for (int i = 0; i < n; i++)
		if (v[i] == 2) {
			if (i > 0 && v[i - 1] == 0) {
				v[i - 1] = 1;
				v[i]--;
			}
			else if (i < n - 1 && v[i + 1] == 0) {
				v[i + 1] = 1;
				v[i]--;
			}
		}

	for (int i : v)
		if (i > 0)
			answer++;

	return answer;
}

int main() {
	int n;
	string input1;
	string input2;
	vector<int> lost;
	vector<int> reserve;

	cin >> n;
	getline(cin, input1);
	getline(cin, input2);

	regex re("[0-9]");
	smatch match;
	
	regex_match(input1, match, re);
	while (regex_search(input1, match, re)) {
		lost.push_back(stoi(match.str()));
		input1 = match.suffix();
	}

	regex_match(input2, match, re);
	while (regex_search(input2, match, re)) {
		reserve.push_back(stoi(match.str()));
		input2 = match.suffix();
	}

	solution(n, lost, reserve);
}