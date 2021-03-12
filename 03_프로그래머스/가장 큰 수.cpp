// https://programmers.co.kr/learn/courses/30/lessons/42746


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int compare(string n1, string n2) {
	int min_size = min(n1.size(), n2.size());
	int ret;

	for (int i = 0; i < min_size; i++) {
		ret = n1[i] > n2[i];

		if (ret != 0)
			return ret;
	}

	return n1.size() > n2.size();
}

string solution(vector<int> numbers) {
	string answer = "";
	vector<string> numbers2str;

	for (int num : numbers)
		numbers2str.push_back(to_string(num));

	sort(numbers2str.begin(), numbers2str.end(), compare);

	for (auto num : numbers2str)
		answer += num;

	for (int i = 0; i < answer.size(); i++) {
		if (answer[i] != '0' || i == answer.size() - 1) {
			answer = answer.substr(i);
			break;
		}
	}

	return answer;
}


// test
int main() {

}
