// https://programmers.co.kr/learn/courses/30/lessons/12985


#include <iostream>
#include <cstdlib>

using namespace std;


int solution(int n, int a, int b) {
	int round = 1;

	a -= 1;
	b -= 1;

	while (int(a / 2) != int(b / 2)) {
		a = int(a / 2);
		b = int(b / 2);
		round += 1;
	}

	return round;
}


int main()
{
	return 0;
}