// https://programmers.co.kr/learn/courses/30/lessons/49993


#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int solution(string skills, vector<string> skill_trees) {
	int answer = 0;
	map<char, int> m;
	set<char> s;

	for (int i = 0; i < skills.size(); i++) {
		m.insert(make_pair(skills[i], i));
		s.insert(skills[i]);
	}

	for (auto skill_tree : skill_trees) {
		int cnt = 0;

		for (auto skill : skill_tree)
			if (s.find(skill) != s.end())
				if (cnt == m[skill])
					cnt++;
				else
					cnt = -1;

		if (cnt != -1)
			answer++;
	}

	return answer;
}


// test
int main() {
	string arg1 = "CBD";
	vector<string> arg2{ "BACDE", "CBADF", "AECB", "BDA" };
	
	cout << solution(arg1, arg2);	// expected output: 2
}
