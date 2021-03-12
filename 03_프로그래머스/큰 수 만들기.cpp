// https://programmers.co.kr/learn/courses/30/lessons/42860


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
	string answer = "";
	int n = number.size();
	int s = 0;

	for (int i = 0; i < n - k; i++) {
		char max_value = number[s];

		for (int j = s + 1; j <= i + k; j++)
			if (max_value < number[j]) {
				max_value = number[j];
				s = j;
			}

		answer += max_value;
		s++;
	}

	return answer;
}

// test
int main() {
}
