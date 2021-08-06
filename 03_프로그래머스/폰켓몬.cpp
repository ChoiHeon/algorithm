// 문제: https://programmers.co.kr/learn/courses/30/lessons/1845?language=cpp

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<int> nums) {
	int ret = nums.size() / 2;
	unordered_set<int> set;

	for (int ele : nums)
		set.insert(ele);

	return ret < set.size() ? ret : set.size();
}

int main() {
	
	return 0;
}
