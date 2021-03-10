// https://programmers.co.kr/learn/courses/30/lessons/42839


#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <unordered_set>

using namespace std;

bool prime(int n) {
	if (n <= 1)
		return false;

	int k = sqrt(n);

	for (int i = 2; i <= k; i++)
		if (n % i == 0)
			return false;

	return true;
}

int solution(string numbers) {
	int answer = 0;
	int n = numbers.size();
	unordered_set<int> s;

	sort(numbers.begin(), numbers.end());

	do {
		string sub = "";

		for (int i = 0; i < n; i++) {
			sub += numbers[i];
			s.insert(stoi(sub));
		}

	} while (next_permutation(numbers.begin(), numbers.end()));

	for (auto i : s)
		if (prime(i))
			answer++;

	return answer;
}


// test
int main() {
	cout << prime(97) << endl;
}
