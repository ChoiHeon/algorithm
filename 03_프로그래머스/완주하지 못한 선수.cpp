// 문제: https://programmers.co.kr/learn/courses/30/lessons/42576

#include <regex>

#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	unordered_multiset<string, int> ums;

	for (string str : participant)
		ums.insert(str);
	
	for (string str : completion)
		ums.erase(ums.find(str));

	return *ums.begin();
}

int main() {
	string data1;
	string data2;
	vector<string> participant;
	vector<string> completion;

	getline(cin, data1);
	getline(cin, data2);

	regex re("[a-z]+");
	smatch match;
	
	regex_match(data1, match, re);
	while (regex_search(data1, match, re)) {
		participant.push_back(match.str());
		data1 = match.suffix();
	}

	regex_match(data2, match, re);
	while (regex_search(data2, match, re)) {
		completion.push_back(match.str());
		data2 = match.suffix();
	}

	cout << solution(participant, completion) << endl;
}