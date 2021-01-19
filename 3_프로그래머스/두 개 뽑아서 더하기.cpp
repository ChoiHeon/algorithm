// 문제: https://programmers.co.kr/learn/courses/30/lessons/68644

#include <iostream>
#include <string>
#include <set>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
	set<int> s;
	vector<int> answer;

	int n = numbers.size();
	for (int i = 0; i < n - 1; i++)
		for (int j = i + 1; j < n; j++)
			s.insert(numbers[i] + numbers[j]);

	answer.assign(s.begin(), s.end());

	return answer;
}

int main() {
	string data;
	vector<int> numbers;

	cin >> data;

	for (char c : data)
		if (isdigit(c))
			numbers.push_back(c - '0');

	for (int num : numbers)
		cout << num;

	getchar();
}