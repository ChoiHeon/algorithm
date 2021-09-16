// https://programmers.co.kr/learn/courses/30/lessons/85002

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> weights, vector<string> head2head) {
	const int n = weights.size();

	vector<float> p(n);
	vector<int> q(n);
	vector<int> answer;

	for (int i = 0; i < n; i++) {
		int r = 0;
		answer.push_back(i);

		for (int j = 0; j < n; j++) {
			if (head2head[i][j] == 'N')
				continue;
			++r;
			if (head2head[i][j] == 'W') {
				++p[i];
				if (weights[i] < weights[j])
					++q[i];
			}
		}

		if (r != 0)
			p[i] /= r;
	}

	sort(answer.begin(), answer.end(), [&](int i, int j)->bool {
		if (p[i] != p[j])
			return p[i] > p[j];
		if (q[i] != q[j])
			return q[i] > q[j];
		if (weights[i] != weights[j])
			return weights[i] > weights[j];
		return i < j;
	});

	for (vector<int>::iterator itr = answer.begin(); itr != answer.end(); ++itr)
		++(*itr);

	return answer;
}

int main() {

	return 0;
}