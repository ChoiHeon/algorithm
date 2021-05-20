// https://programmers.co.kr/learn/courses/30/lessons/42842


#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

vector<int> solution(int brown, int yellow) {
	int w, h;
	int sqt = sqrt(yellow);
	int total = brown + yellow;
	vector<int> answer;

	for (h = 1; h <= sqt; h++) {
		if (yellow % h != 0)
			continue;

		w = yellow / h;

		if ((w + 2)*(h + 2) == total) {
			answer.push_back(w + 2);
			answer.push_back(h + 2);
			break;
		}
	}

	return answer;
}


int main()
{
}