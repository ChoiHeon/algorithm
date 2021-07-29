// 문제: https://www.acmicpc.net/problem/1786

#include <iostream>
#include <string>
#include <memory.h> // for using memset()
#include <vector>

using namespace std;

int n, m;
int lps[1000000]; // lps = longest-prefix & suffix
string t;
string p;

void InitializeLPS() {
	int j = 0;
	memset(lps, 0, sizeof(lps));

	for (int i = 1; i < m; i++) {
		while (0 < j && p[i] != p[j])
			j = lps[j - 1];

		if (p[i] == p[j]) {
			j++;
			lps[i] = j;
		}
	}
}

void KMP() {
	InitializeLPS();

	int j = 0;
	vector<int> answer;

	for (int i = 0; i < n; i++) {
		while (j > 0 && t[i] != p[j])
			j = lps[j - 1];

		if (t[i] == p[j]) {
			j++;

			if (j == m) {
				answer.push_back(i - m + 2);
				j = lps[m - 1];
			}
		}
	}

	cout << answer.size() << "\n";
	for (int e : answer)
		cout << e << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	getline(cin, t);
	getline(cin, p);

	n = t.length();
	m = p.length();

	KMP();

	return 0;
}