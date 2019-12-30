#include "pch.h"
#include <iostream>
#include <cstring>
#include <string>
#include <math.h>
#include <algorithm>
#include <numeric>

using namespace std;

//=============================================================================
void LIS(int n, int* array);

int main()
{

	int test_count;	 // 반복할 횟수
	int input_count; // 남은 반복 횟수

	cin >> test_count;
	input_count = test_count;

	// test
	while (input_count != 0)
	{
		int n;			// input size 1
		int* array;		// input size 2

		cin >> n;

		array = new int[n + 1];	// index 0은 사용하지 않음
								// 큰 의미 없이, 가독성을 위함임

		for (int i = 1; i <= n; i++)
			cin >> array[i];

		LIS(n, array);			// 알고리즘 함수 실행

		delete[] array;			// 배열 할당 해제

		input_count--;			// 반복 횟수 차감
	}

	return 0;
}

void LIS(int n, int* array)
{
	int result = 0;							 // 반환할 값을 저장

	int* max_count_column = new int[n + 1];  /*
											 max_count_column[j] : (k < j)
																	count[1 ~ k][j]중
																	가장 큰 값
											 */

	int** count = new int*[n + 1];			 /*
											 count[i][i] : index 1 ~ i까지의
															부분 수열 중에서 
															가장 길이가 긴 값
											 count[i][j] : (i < j)
															array[i]와 array[j]를
															포함하는 부분 수열 중
															가장 길이가 긴 값
											 */

	// 배열 초기화
	memset(max_count_column, 0, sizeof(int) * (n + 1));

	for (int i = 0; i <= n; i++) 
	{
		count[i] = new int[n + 1];
		memset(count[i], 0, sizeof(int) * (n + 1));
	}

	// 동적 프로그래밍을 사용
	for (int i = 1; i <= n; i++)
	{
		count[i][i] = max_count_column[i];

		for (int j = i + 1; j <= n; j++)
		{
			if (array[i] < array[j])
			{
				count[i][j] = count[i][i] + 1;

				// result 업데이트
				if (count[i][j] > result)
					result = count[i][j];

				// max_count_column 업데이트
				if (count[i][j] > max_count_column[j])
					max_count_column[j] = count[i][j];
			}
		}
	}
	
	// 결과 출력
	cout << result + 1 << endl << endl;
}