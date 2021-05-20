#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <cstdlib>
#include <algorithm>

using namespace std;

int solution(int n, vector<string> data) {
	bool f;
	char a, b;
	char p;
	int x, y;
	int d;
	int answer = 0;
	vector<char> friends{ 'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T' };

	sort(friends.begin(), friends.end());

	do {
		answer++;

		for (int i = 0; i < n; i++) {
			a = data[i][0];
			b = data[i][2];
			p = data[i][3];
			d = data[i][4] - '0';

			for (int j = 0; j < 8; j++) {
				if (friends[j] == a)
					x = j;
				else if (friends[j] == b)
					y = j;
			}

			f = false;

			switch (p) {
			case '<':
				f = (abs(x - y) - 1) < d;
				break;
			case '>':
				f = (abs(x - y) - 1) > d;
				break;
			case '=':
				f = (abs(x - y) - 1) == d;
				break;
			default:
				break;
			}

			if (!f) {
				answer--;
				break;
			}
		}
	} while (next_permutation(friends.begin(), friends.end()));

	return answer;
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	vector<string> data;
}