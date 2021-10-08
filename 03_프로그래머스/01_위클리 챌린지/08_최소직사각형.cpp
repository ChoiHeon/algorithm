// https://programmers.co.kr/learn/courses/30/lessons/86491

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int solution(vector<vector<int>> sizes) {
	int w = 0;
	int h = 0;

	for (auto& card : sizes)
		if (card[0] > card[1])
			swap(card[0], card[1]);

	for (auto& card : sizes) {
		w = max(card[0], w);
		h = max(card[1], h);
	}

	return w * h;
}

int main() {

	return 0;
}