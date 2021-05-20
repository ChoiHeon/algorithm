// https://programmers.co.kr/learn/courses/30/lessons/12973?language=cpp

#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

string toString(vector<char> v) {
	string ret;
	for (char c : v)
		ret += c;
	return ret;
}

int solution(string str)
{
	vector<char> stack;

	for (char ch : str) {
		if (stack.empty()) {
			stack.push_back(ch);
		}
		else if (stack.back() == ch) {
			stack.pop_back();
		}
		else {
			stack.push_back(ch);
		}
	}

	return stack.empty() ? 1 : 0;
}


int main()
{
	cout << solution("baabaa") << endl;;
	cout << solution("cdcd") << endl;
}