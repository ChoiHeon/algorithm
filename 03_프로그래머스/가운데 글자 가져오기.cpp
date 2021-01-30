// 문제: https://programmers.co.kr/learn/courses/30/lessons/12903

#include <regex>
#include <iostream>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
	int len = s.length();

	if (len % 2 == 0)
		return s.substr(len / 2 - 1, 2);
	return s.substr(len / 2 - 1, 1);
}

int main() {
	
}