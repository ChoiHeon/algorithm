// https://programmers.co.kr/learn/courses/30/lessons/42860


#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

#define min(a, b) (a < b ? a : b)

using namespace std;


int solution(string name) {
	int answer = 0;
	int cursor = 0;
	string current(name.size(), 'A');

	while (current != name) {
		int dist = 20;
		int temp = -1;
		int target = -1;

		for (int i = 0; i < name.size(); i++) {
			if (current[i] == name[i])
				continue;

			temp = min(abs(cursor - i), abs(((int)(name.length() - 1) - i + cursor + 1)));
			if (temp < dist) {
				dist = temp;
				target = i;
			}
		}

		answer += dist;
		answer += min(abs(name[target] - current[target]), 90 - name[target] + 1);
		current[target] = name[target];
		cursor = target;
	}

	return answer;
}


int main()
{
	cout << solution("JEROEN") << endl;
}