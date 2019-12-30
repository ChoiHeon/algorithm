#include "pch.h"
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <numeric>

using namespace std;

//=============================================================================

void Boggle(string word, int apb_count[26], int apb_position[][2][25]);
bool Search(string word, int index, int current_x, int current_y,int apb_count[26], int apb_position[][2][25]);
bool IsAround(int x1, int y1, int x2, int y2);

int main()
{
	
	int test_count;
	int input_count;

	cin >> test_count;
	input_count = test_count;

	// test
	while (input_count != 0)
	{
		char board[5][5];					// BOGGLE 게임판
		int word_count;						// 입력 받을 단어 개수
		vector<string> word_array;

		int alphabet_count[26] = { 0, };	// board의 각 알파벳의 개수
		int alphabet_position[26][2][25];	// 각 알파벳의 좌표
		memset(alphabet_position, 0, sizeof(alphabet_position)); // 3차원 배열 초기화

		// 보드 입략
		char c;
		for (int i = 0; i < 5; i++)
			for (int j = 0; j < 5; j++)
			{
				cin >> c;

				board[i][j] = c;	// 보드 저장
				alphabet_position[c - 65][0][alphabet_count[c - 65]] = i;	// 입력한 알파벳에 대한 좌표 저장(x)
				alphabet_position[c - 65][1][alphabet_count[c - 65]] = j;	// 입력한 알파벳에 대한 좌표 저장(y)

				alphabet_count[c - 65]++;	// 입력한 알파벳 개수 카운트
			}

		flush(cout); // 입력 버프 제거

		// 단어 입력
		cin >> word_count;

		// 단어 저장
		string word;
		for (int i = 0; i < word_count; i++)
		{
			cin >> word;
			word_array.push_back(word);
		}


		// 결과 출력
		cout << endl;
		for (int i = 0; i < word_count; i++)
		{
			Boggle(word_array[i], alphabet_count, alphabet_position);
		}

		input_count--;
	}
	
	
	
	return 0;
}

void Boggle(string word, int apb_count[26], int apb_position[][2][25])
{
	char current = word[0];	// 맨 앞의 알파벳
	int current_x;			// 좌표(x)
	int current_y;			// 좌표(y)
	bool result = false;	// 결과 판단할 변수

	// 모든 current에 대해서 Search함수 실행
	for (int i = 0; i < apb_count[current - 65]; i++)
	{
		current_x = apb_position[current - 65][0][i];
		current_y = apb_position[current - 65][1][i];

		// Search를 통해 하나라도 true를 발견할 경우, result를 true로 변경
		result = result || Search(word, 0, current_x, current_y, apb_count, apb_position);
	}

	// result에 따른 출력
	cout << word;
	result ? cout << " YES" : cout << " NO";
	cout << endl;

}

bool Search(string word, int index, int current_x, int current_y, int apb_count[26], int apb_position[][2][25])
{
	// 단어를 찾음
	if (word.length() == index + 1)
		return true;

	// 다음 알파벳이 있는지 확인
	char current = word[index];
	char next = word[index + 1];
	int next_x;
	int next_y;
	bool result = false;

	// 재귀 시작
	for (int i = 0; i < apb_count[next - 65]; i++)
	{
		next_x = apb_position[next - 65][0][i];
		next_y = apb_position[next - 65][1][i];

		// current 주변에 next가 있는지 판단, 있을 경우, 재귀적으로 Search 실행 
		if (IsAround(current_x, current_y, next_x, next_y))
			result = result || Search(word, ++index, next_x, next_y, apb_count, apb_position);
	}

	return result;
}

bool IsAround(int x1, int y1, int x2, int y2)
{
	if (abs(x1 - x2) <= 1 && abs(y1 - y2) <= 1)
		return true;

	return false;
}