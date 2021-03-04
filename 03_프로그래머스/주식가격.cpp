// https://programmers.co.kr/learn/courses/30/lessons/42584


#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer;

	for (int i = 0; i < prices.size(); i++) {
		int term = 0;

		for (int j = i + 1; j < prices.size(); j++) {
			term++;

			if (prices[j] < prices[i])
				break;
		}

		answer.push_back(term);
	}

	return answer;
}

// test
int main() {

	return 0;
}
