// https://programmers.co.kr/learn/courses/30/lessons/42747


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
	int n = citations.size();
	int answer = -1;

	sort(citations.begin(), citations.end());

	for (int i = 0; i < n; i++) {
		if (citations[i] <= n - i) 
			answer = max(answer, citations[i]);
		else 
			answer = max(answer, n - i);
	}
	
	return answer;
}

// test
int main() {
	vector<int> input{ 22, 42 };
	vector<int> input2{ 3, 0, 6, 1, 5 };
	cout << solution(input) << endl;
	cout << solution(input2) << endl;
}
