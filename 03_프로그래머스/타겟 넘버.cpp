// https://programmers.co.kr/learn/courses/30/lessons/43165?language=cpp


#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers, int target) {
	int m, x;
	deque<int> stack(1);
	
	for (auto y : numbers) {
		m = stack.size();

		for (int i = 0; i < m; i++) {
			x = stack.front();
			stack.pop_front();

			stack.push_back(x + y);
			stack.push_back(x - y);
		}
	}

	return count(stack.begin(), stack.end(), target);
}


int main()
{

	return 0;
}