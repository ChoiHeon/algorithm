// https://programmers.co.kr/learn/courses/30/lessons/77885

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;


void to_binary(vector<int>& v, long long x) {
	v.clear();

	do {
		v.push_back(x % 2);
		x /= 2;
	} while (x);
}


vector<long long> solution(vector<long long> numbers) {
	vector<long long> answer;
	vector<long long> pow_2(1, 1LL);
	vector<int> bi;

	for (int i = 0; i < 50; i++)
		pow_2.push_back(pow_2.back() + pow_2.back());

	int i, j;
	bool flag;

	for (auto num : numbers) {
		to_binary(bi, num);

		i = 0;
		j = -1;

		for (; i < bi.size(); i++) {
			if (bi[i] == 0)
				break;

			j = i;
		}

		if (j >= 0)
			num -= pow_2[j];
		num += pow_2[i];

		answer.push_back(num);
	}

	return answer;
}