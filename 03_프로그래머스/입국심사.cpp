// https://programmers.co.kr/learn/courses/30/lessons/1832

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
	long long low, mid, high;
	long long count;
	long long answer;

	sort(times.begin(), times.end());

	low = 1;
	high = times.back() * (long long)n;
	answer = high;

	while (low < high) {
		mid = (low + high) / 2;
		count = 0;

		for (int i = 0; i < times.size(); i++)
			count += (mid / times[i]);

		if (n <= count) {
			answer = mid;
			high = mid;
		}
		else
			low = mid + 1;
	}

	return answer;
}

int main() {
	vector<vector<int>> m(3, vector<int>(10, 3));
	cout << m[2][3];
}