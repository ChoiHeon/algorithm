// https://www.acmicpc.net/problem/1918


#include <iostream>
#include <stack>
#include <string>
#include <ctype.h>

using namespace std;



int main() {
	string s, answer;
	stack<char> st;

	cin >> s;

	for (char c : s) {
		if (isalpha(c)) {
			answer.push_back(c);
		}
		else {
			if (c == '(') {
				st.push(c);
			}
			else if (c == '*' || c == '/') {
				while (!st.empty() && (st.top() == '*' || st.top() == '/')) {
					answer.push_back(st.top());
					st.pop();
				}
				st.push(c);
			}
			else if (c == '+' || c == '-') {
				while (!st.empty() && st.top() != '(') {
					answer.push_back(st.top());
					st.pop();
				}
				st.push(c);
			}
			else {  // if x == ')'
				while (st.top() != '(') {
					answer.push_back(st.top());
					st.pop();
				}
				st.pop();
			}
		}
	}
	
	while (!st.empty()) {
		answer.push_back(st.top());
		st.pop();
	}

	cout << answer << endl;

	return 0;
}