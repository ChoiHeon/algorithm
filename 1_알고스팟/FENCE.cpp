#include <iostream>
#include <cstring>
#include <string>
#include <set>

using namespace std;

//=============================================================================

void cutFence(int len, int* fences);

int main()
{
	int test_count;	 // 반복할 횟수
	int input_count; // 남은 반복 횟수

	cin >> test_count;
	input_count = test_count;

	// test
	while (input_count != 0)
	{
		int count;
		int* fences;	// 인덱스 0 사용하지 않음
		int input;

		cin >> count;

		fences = new int[count + 1];
		fences[0] = -1;

		for (int i = 1; i <= count; i++)
		{
			cin >> fences[i];
		}

		cutFence(count, fences);

		input_count--;			// 반복 횟수 차감
	}

	return 0;
}

void cutFence(int len, int* fences)
{
	int w;
	int h;
	int max_size = 0;

	for (int i = 1; i <= len; i++)
	{
		w = 1;
		h = fences[i];
		int j = i - 1;
		int k = i + 1;

		// left check
		while (1 <= j && h <= fences[j])
		{
			w++; j--;
		}

		// right check
		while (k <= len && h <= fences[k])
		{
			w++; k++;
		}
		
		// update max_size
		if (max_size <= (w * h))
			max_size = w * h;
;	}

	cout << max_size << endl;
}