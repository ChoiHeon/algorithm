#include "pch.h"
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

int main()
{
	int test_count;
	int input_count;
	vector<int> student_number;	// 학생 수
	vector<int> friend_number;	// 친구 수
	vector<vector<int>> friend_map;	// 친구 짝 

	cin >> test_count;
	input_count = test_count;

	// Input
	while (input_count != 0)
	{
		int n, m, map_value;
		string str;
		vector<int> v;

		cin >> n >> m;
		student_number.push_back(n);
		friend_number.push_back(m);

		for (int i = 0; i < m * 2; i++)
		{
			cin >> map_value;
			v.push_back(map_value);
		}

		friend_map.push_back(v);

		input_count--;
	}

	// Searsh
	input_count = test_count;

	while (input_count != 0) {
		int index = test_count - input_count;
		int n = student_number[index];
		int m = friend_number[index];
		int sum = pow(n * (n - 1) / 2, 2); // 세제곱근 합
		int result = 0;

		
		vector<int> map(friend_map[index]);
		vector<int> comb(m, 0); // length -> m / initialize -> 0

		for (int i = 1; i <= (n / 2); i++) // comb = { 0, 0, ...., 1, 1 } / 1의 개수는 이룰 수 있는 짝의 수
			comb[m - i] = 1;

		do
		{
			int temp = 0;

			for (int i = 0; i < m; i++)
				temp += comb[i] * (pow(map[2 * i], 3) + pow(map[2 * i + 1], 3)); // 짝을 이루는 수(n1, n2)의 세제곱 합을 구함 & 이를 모두 더함

			if (temp == sum) // 같으면 실제로 생성이 가능한 정렬
				result++;

		} while (next_permutation(comb.begin(), comb.end())); // comb의 길이 : m / mPm을 구하는 while문

		cout << "result : " << result << endl;

		input_count--;
	}


	return 0;
}
