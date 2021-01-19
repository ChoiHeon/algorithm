// 문제: https://programmers.co.kr/learn/courses/30/lessons/42840

#include <regex>
#include <iostream>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
	int student[3][10] = {
		{1, 2, 3, 4, 5},
		{2, 1, 2, 3, 2, 4, 2, 5,},
		{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
	};
	int cnt[3] = { 5, 8, 10 };
	vector<int> answer;
	vector<int> score{ 0, 0, 0 };
	int max_score = -1;
		
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < answers.size(); j++)
			if (student[i][j % cnt[i]] == answers[j]) 
				score[i]++;

	max_score = *max_element(score.begin(), score.end());

	for (int i = 0; i < 3; i++)
		if (score[i] == max_score)
			answer.push_back(i + 1);

	return answer;
}

int main() {
	string input;
	vector<int> answers;

	getline(cin, input);

	regex re("[0-9]");
	smatch match;
	
	regex_match(input, match, re);
	while (regex_search(input, match, re)) {
		answers.push_back(stoi(match.str()));
		input = match.suffix();
	}

	solution(answers);
}