#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>

using namespace std;

//=============================================================================

vector<char> transQuadTree();
vector<char> operator+(vector<char> v1, vector<char> v2);
void printQuadTree(vector<char> v);

queue<char> q;

int main()
{
	int test_count;	 // 반복할 횟수
	int input_count; // 남은 반복 횟수

	cin >> test_count;
	input_count = test_count;

	// test
	while (input_count != 0)
	{
		string input;
		vector<char> input2;
		cin >> input;


		for (int i = 0; i < input.length(); i++)
			q.push(input[i]);

		printQuadTree(transQuadTree());

		input_count--;			// 반복 횟수 차감
	}

	return 0;
}

vector<char> transQuadTree()
{
	vector<char> v;
	v.push_back(q.front());
	q.pop();

	if (v.back() == 'x')
	{
		vector<char> v1 = transQuadTree();	// left  up
		vector<char> v2 = transQuadTree();  // right up
		vector<char> v3 = transQuadTree();  // left  down
		vector<char> v4 = transQuadTree();  // right down

		return v + v3 + v4 + v1 + v2;		// transform shape
	}
	else
	{
		return v;						    // base case
	}
}

vector<char> operator+(vector<char> v1, vector<char> v2)
{
	vector<char> result;

	for (vector<char>::iterator itr = v1.begin(); itr != v1.end(); itr++)
		result.push_back(*itr);

	for (vector<char>::iterator itr = v2.begin(); itr != v2.end(); itr++)
		result.push_back(*itr);

	return result;
}

void printQuadTree(vector<char> qt)
{
	for (vector<char>::iterator itr = qt.begin(); itr != qt.end(); itr++)
		cout << *itr;
	cout << endl;
}
