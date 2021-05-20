// https://programmers.co.kr/learn/courses/30/lessons/1832

#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

vector<int> solution(int n, vector<string> words) {
	vector<int> answer(2, 0);
	unordered_set<string> used;
	used.insert(words[0]);

	for (int i = 1; i < words.size(); i++) {
		if (words[i - 1].back() != words[i].front()
			|| used.find(words[i]) != used.end()) {
			answer[0] = i % n + 1;
			answer[1] = i / n + 1;
			break;
		}

		used.insert(words[i]);
	}

	return answer;
}


void main() {
	string str = "hello";
	cout << str.back() << endl;
	cout << str.front();
}