#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

//=============================================================================

bool JumpGame(int width, int** board);

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
		int width;
		cin >> width;

		// 이차원 배열 board 할당
		int** board = new int*[width];
		for (int i = 0; i < width; i++)
			board[i] = new int[width];

		// board 값 입력
		int input;
		for (int i = 0; i < width; i++)
			for (int j = 0; j < width; j++)
				cin >> board[i][j];

		if (JumpGame(width, board))
			cout << "YES" << endl;
		else
			cout << "NO" << endl;

		//=============================================================================

		input_count--;			// 반복 횟수 차감
	}

	return 0;
}

bool JumpGame(int width, int** board)
{
	// 이동 가능성 확인
	bool** check = new bool*[width];
	for (int i = 0; i < width; i++)
	{
		check[i] = new bool[width];
		memset(check[i], false, sizeof(bool) * width); // check를 false로 초기화
	}

	// [0][0]은 제외
	check[0][0] = true;

	int i = 0;
	int j = 0;
	int dis;
	for (int i = 0; i < width; i++)
		for (int j = 0; j < width; j++)
			if (check[i][j])
			{
				dis = board[i][j];
				if (j + dis < width)
					check[i][j + dis] = true;
				if (i + dis < width)
					check[i + dis][j] = true;
			}

	return check[width - 1][width - 1];
}