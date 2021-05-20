// https://programmers.co.kr/learn/courses/30/lessons/42578

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;


// 공식 적용 X
/*int solution(vector<vector<string>> clothes) {
	int n;
	int id = 0;
	int answer = 0;
	unordered_map<string, int> type_id;
	vector<int> cnt;
	vector<int> cmb;

	for (auto cloth : clothes) {
		if (type_id.find(cloth[1]) == type_id.end()) {
			type_id[cloth[1]] = id++;
			cnt.push_back(1);
		}
		else {
			cnt[type_id[cloth[1]]] += 1;
		}
	}

	n = type_id.size();
	cmb.assign(n, 0);
	int temp;

	for (int i = n-1; 0 <= i; i--) {
		cmb[i] = 1;

		do {
			temp = 1;

			for (int j = 0; j < n; j++)
				if (cmb[j])
					temp *= cnt[j];

			answer += temp;
		} while (next_permutation(cmb.begin(), cmb.end()));
	}

	return answer;
}*/

// 공식 적용 O
int solution(vector<vector<string>> clothes) {
	int answer = 1;
	unordered_map<string, int> m;

	for (auto cloth : clothes)
		m[cloth[1]] += 1;

	for (auto p : m)
		answer *= (p.second + 1);

	return answer - 1;
}


int main() {
	unordered_map<string, int> m;
	cout << m["S"] << endl;
}