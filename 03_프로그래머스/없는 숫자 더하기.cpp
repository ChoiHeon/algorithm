#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

class AAA {
public :
	virtual void foo() abstract;
};

int solution(vector<int> numbers) {
	int bm = 0;
	int answer = 0;
	for (int num : numbers)
		bm |= (1 << (num + 1));
	for (int i = 1; i <= 10; ++i)
		if (bm & (1 << i))
			answer += i;
	return answer;
}

int main() {

	return 0;
}