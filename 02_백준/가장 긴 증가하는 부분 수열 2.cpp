// https://www.acmicpc.net/problem/12015

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector<int> arr;

int solution() {
	int result;
	vector<int> lis;

	lis.push_back(arr[0]);

	for (int i = 1; i < n; i++) {
		if (lis.back() < arr[i])
			lis.push_back(arr[i]);
		else {
			auto e = lower_bound(lis.begin(), lis.end(), arr[i]);
			*e = arr[i];
		}
	}

	result = lis.size();
	return result;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;
	arr.reserve(n);

	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		arr.push_back(tmp);
	}

	cout << solution() << endl;

	return 0;
}