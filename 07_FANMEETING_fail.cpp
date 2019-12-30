#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

//=============================================================================

int hugAllMembers(const string& members, const string& fans);

int main()
{

	int test_count;	 // 반복할 횟수
	int input_count; // 남은 반복 횟수

	cin >> test_count;
	input_count = test_count;

	// test
	while (input_count != 0)
	{
		//=============================================================================
		string members;
		string fans;

		cin >> members;
		cin >> fans;

		// 시간 초과
		// cout << hugAllMembers(members, fans) << endl;
		// 카라츠바 알고리즘을 통해 해결해야 함

		//=============================================================================

		input_count--;			// 반복 횟수 차감
	}

	return 0;
}


// 시간 초과
int hugAllMembers(const string& members, const string& fans)
{
	int n = members.length();
	int m = fans.length();

	int result = 0;
	bool flag;

	vector<int> v_members(n);
	vector<int> v_fans(m);

	/*
		M --> 0
		F --> 1

		cuz, if only M | M --> result = 0 / then, is false
	*/

	for (int i = 0; i < n; i++)
		v_members[i] = (members[i] == 'F');

	for (int i = m - 1; i > -1; i--)
		v_fans[i] = (fans[i] == 'F');


	for (int i = 0; i < m - n + 1; i++)
	{
		flag = true;
		for (int j = 0; j < n; j++)
		{
			if (!(v_members[j] | v_fans[i + j])) // M : M 경우
			{
				flag = false;
				break;
			}
		}

		if (flag)
			result++;
	}

	return result;
}