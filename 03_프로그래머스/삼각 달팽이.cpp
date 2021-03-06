// https://programmers.co.kr/learn/courses/30/lessons/68645


#include <iostream>
#include <string>
#include <vector>


using namespace std;

vector<int> solution(int n) {
	vector<int> answer;
	vector<vector<int>> triangle;


	for (int i = 0; i < n; i++) {
		vector<int> v;
		triangle.push_back(v);

		for (int j = 0; j <= i; j++)
			triangle[i].push_back(0);
	}

	int num = 1;
	int m = n;
	int i = 0, j = 0;

	while (m > 0) {
		if (m == 1) {
			triangle[i][j] = num;
			break;
		}

		for (int k = 0; k < m - 1; k++)
			triangle[i + k][j] = (num++);

		for (int k = 0; k < m - 1; k++)
			triangle[i + m - 1][j + k] = (num++);

		for (int k = 0; k < m - 1; k++)
			triangle[i + m - k - 1][j + m - k - 1] = (num++);

		m -= 3;
		i += 2;
		j += 1;
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j <= i; j++)
			answer.push_back(triangle[i][j]);

	return answer;
}


// test
int main() {
}
