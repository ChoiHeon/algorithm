// 문제: https://programmers.co.kr/learn/courses/30/lessons/42748

#include <regex>
#include <iostream>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer;
	vector<int> sub;
	int i, j, k;

	for (auto command: commands) {
		i = command[0];
		j = command[1];
		k = command[2];

		for (auto itr = array.begin() + i - 1; itr != array.begin() + j; itr++)
			sub.push_back(*itr);

		sort(sub.begin(), sub.end());
		answer.push_back(sub[k - 1]);

		sub.clear();
	}


	return answer;
}

int main() {
	/*int n;
	string input1;
	string input2;
	vector<int> array;
	vector<vector<int>> commands;

	for (int i = 0; i < 3; i++) {
		int tmp;
		cin >> tmp;
		array.push_back(tmp);
	}

	for (int i = 0; i < 3; i++) {
		vector<int> v;
		commands.push_back(v);

		for (int j = 0; j < 3; j++) {
			int tmp;
			cin >> tmp;
			commands[i].push_back(tmp);
		}
	}

	solution(array, commands);*/

	vector<int> v{ 5, 4, 3, 2, 1 };
	sort(v.begin(), v.begin() + 4);

	for (int e : v)
		cout << e << ", ";
}