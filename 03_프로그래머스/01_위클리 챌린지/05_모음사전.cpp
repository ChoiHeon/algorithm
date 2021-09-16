// https://programmers.co.kr/learn/courses/30/lessons/84512

#include <iostream>
#include <cmath>
#include <string>
#include <map>

using namespace std;

int geometricSum(int k) {
	return (pow(5, k)-1) / 4;
}

int solution(string word) {
	int n = word.size();
	int answer = 0;
	map<char, int> order = { {'A', 0}, {'E', 1 }, {'I', 2}, {'O', 3}, {'U', 4} };

	for (int i = 0; i < n; i++)
		answer += order[word[i]] * geometricSum(5-i)+ 1;
	
	return answer;
}

int main() {

	cout << solution("AAAE") << endl;
	cout << solution("EIO") << endl;

	return 0;
}