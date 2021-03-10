// https://programmers.co.kr/learn/courses/30/lessons/42626


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define heapify(v) make_heap(v.begin(), v.end(), greater<int>())
#define heappop(v) pop_heap(v.begin(), v.end(), greater<int>())
#define heappush(v) push_heap(v.begin(), v.end(), greater<int>())

int solution(vector<int> v, int k) {
	int answer = 0;
	
	make_heap(v.begin(), v.end(), greater<int>());

	while (v.front() < k) {
		int e1, e2, e3;

		e1 = v.front();
		heappop(v);
		v.pop_back();

		e2 = v.front();
		heappop(v);
		v.pop_back();

		e3 = e1 + 2 * e2;
		v.push_back(e3);
		heappush(v);

		answer++;
	}

	return answer;
}


// test
int main() {

}
