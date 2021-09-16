#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<int> enter, vector<int> leave) {
	int n = enter.size();
	vector<int> answer(n);
	set<int> room;

	for (int i = 0, j = 0; i < n; i++) {
		room.insert(enter[i]);
		
		while (j < n && room.find(leave[j]) != room.end()) {	// 나갈 수 있따면 무조건 방을 나감
			room.erase(leave[j]);
			answer[leave[j] - 1] += room.size();	// 나가는 leave[j]는 방 안의 사람들과 무조건 보았음

			for (auto p : room)
				answer[p - 1] += 1;					// p는 나가는 leave[j]과 무조건 보았음

			j++;
		}
	}

	return answer;
}

int main() {


	return 0;
}