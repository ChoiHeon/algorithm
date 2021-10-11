// https://www.acmicpc.net/problem/11053


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


void setIO() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
}


int main() {
	int n;
	vector<int> v;

	setIO();

	cin >> n;

	for (int x, i = 0; i < n; ++i) {
		cin >> x;

		if (v.empty() || x > v.back()) {
			v.push_back(x);
		}
		else {
			auto itr = lower_bound(v.begin(), v.end(), x);
			*itr = x;
		}
	}

	cout << v.size() << endl;

	return 0;
}