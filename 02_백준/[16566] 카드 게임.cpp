// https://www.acmicpc.net/problem/16566

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int n, m, k;
vector<int> card;
vector<int> upper;
set<int> used;

int find(int x) {
	if (used.find(card[upper[x]]) == used.end()) 
		return upper[x];
	return upper[x] = find(card[upper[x]]);
}

int main() {

	scanf("%d %d %d", &n, &m, &k);

	// initizlize card
	card.assign(m, 0);
	for (int i = 0; i < m; i++) 
		scanf("%d", &card[i]);
	sort(card.begin(), card.end());

	// initialize upper
	upper.assign(n, 0);
	for (int i = 0, j = 0; i < m; i++) {
		while (j < card[i]) {
			upper[j] = i;
			j++;
		}
	}

	// solve
	for (int i = 0; i < k; i++) {
		int x, y;
		scanf("%d", &x);
		y = find(x);
		printf("%d\n", card[y]);
		used.insert(card[y]);
	}

	return 0;
}


