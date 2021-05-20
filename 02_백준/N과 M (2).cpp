// https://www.acmicpc.net/problem/15650

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int m, n;
	vector<int> v;

	cin >> n >> m;

	v.assign(n, 0);
	
	for (int i = 0; i < n-m; i++)
		v[n - i - 1] = 1;

	do {
		for (int i = 0; i < n; i++)
			if (v[i] == 0)
				cout << i + 1 << ' ';
		cout << endl;
	} while (next_permutation(v.begin(), v.end()));

	return 0;
}