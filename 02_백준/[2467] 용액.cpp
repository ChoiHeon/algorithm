#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

#define P(a, b) make_pair(a, b)
typedef pair<int, int> pii;


pii solution(int n, vector<int>& liq) {
	int min_value = 0x7f7f7f7f;
	int low = 0;
	int high = n - 1;
	pii result;

	while (low < high) {
		if (abs(liq[low] + liq[high]) < min_value) {
			min_value = abs(liq[low] + liq[high]);
			result = P(liq[low], liq[high]);
		}

		if (liq[low] + liq[high] < 0)	low++;
		else							high--;
	}

	return result;
}

int main() {
	int n;
	vector<int> liq;

	cin >> n;

	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		liq.push_back(tmp);
	}
		
	pii answer = solution(n, liq);
	printf("%d %d\n", answer.first, answer.second);

	return 0;
}