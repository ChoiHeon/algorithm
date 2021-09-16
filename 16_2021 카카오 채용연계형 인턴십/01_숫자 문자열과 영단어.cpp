// 문제명: 숫자 문자열과 영단어
// 링크: https://programmers.co.kr/learn/courses/30/lessons/81301

#include <iostream>
#include <regex>
#include <string>
#include <map>
#include <vector>

using namespace std;


int solution(string s) {
	int answer = 0;
	map<string, int> word2dgt = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
								 {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
								 {"eight", 8}, {"nine", 9}};
	regex re("zero|one|two|three|four|five|six|seven|eight|nine|\\d", regex::optimize);
	smatch match;

	while (regex_search(s, match, re)) {
		answer = answer * 10 + (isdigit(match.str()[0]) ? stoi(match.str()) : word2dgt[match.str()]);
		s = match.suffix();
	}

	return answer;
}

int main() {

	return 0;
}