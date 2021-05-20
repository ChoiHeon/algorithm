// https://programmers.co.kr/learn/courses/30/lessons/76502


#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
using namespace std;

int solution(string s) {
	bool flag;
	int answer = 0;
	deque<char> queue;
	vector<char> stack;
	map<char, char> dict;

	{
		dict['}'] = '{';
		dict[']'] = '[';
		dict[')'] = '(';
	}

	for (auto c : s)
		queue.push_back(c);

	for (int i = 0; i < s.size(); i++) {
		stack.clear();
		flag = false;
		answer += 1;

		for (auto p : queue) {
			if (p == '(' || p == '[' || p == '{') {
				stack.push_back(p);
			}
			else {
				if (stack.empty() || stack.back() != dict[p]) {
					flag = true;
					break;
				}
				else {
					stack.pop_back();
				}
			}
		}

		if (flag || !stack.empty())
			answer -= 1;

		queue.push_back(queue.front());
		queue.pop_front();
	}

	return answer;
}


int main()
{
}