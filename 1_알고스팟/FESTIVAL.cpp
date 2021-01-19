#include "pch.h"
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <numeric>

using namespace std;

//=============================================================================

double min(double d1, double d2);		// 두 개의 인자 중 작은 값 반환

int main()
{
	int test_count;
	int input_count;
	vector<int> l_array;							// 최소 참가 수 배열
	vector<int> N_array;							// 최대 참가 수 배열
	vector<vector<int>> daily_cost_array;			// 일일 비용 배열 (이중배열)

	cin >> test_count;
	input_count = test_count;

	// Input
	while (input_count != 0)
	{
		int l, N;
		int cost;
		vector<int> daily_cost;

		cin >> N >> l;
		l_array.push_back(l);
		N_array.push_back(N);

		for (int i = 0; i < N; i++)
		{
			cin >> cost;
			daily_cost.push_back(cost);
		}

		daily_cost_array.push_back(daily_cost);

		input_count--;
	}

	// Searsh
	input_count = test_count;
	cout << endl;

	while (input_count != 0) {
		int index = test_count - input_count;
		int l_temp = l_array[index];
		int N_temp = N_array[index];
		vector<int> daily_cost_temp = daily_cost_array[index];

		// 전체 평균 계산, 이외의 큰 값으로 초기화도 가능
		double average = (double)accumulate(daily_cost_temp.begin(), daily_cost_temp.end(), 0) / daily_cost_temp.size();
		
		for (int i = 0; i < N_temp - l_temp + 1; i++)	// i --> 기준 인덱스
		{
			for (int j = l_temp; j <= N_temp; j++)		// j --> 확인 할 배열의 길이
			{
				if (i + j > daily_cost_temp.size())
					break;

				// 기존의 최소 평균 값과 비교
				average = min(average, (double)accumulate(daily_cost_temp.begin() + i, daily_cost_temp.begin() + i + j, 0) / j);  // [i ~ i + j]까지의 평균 vs average
			}
		}

		cout << fixed;				// 소수점 고정
		cout.precision(7);			// 출력 소수 자리 서정
		cout << average << endl;

		input_count--;
	}
	
	return 0;
}

double min(double d1, double d2)
{
	if (d1 <= d2)
		return d1;
	else
		return d2;
}
