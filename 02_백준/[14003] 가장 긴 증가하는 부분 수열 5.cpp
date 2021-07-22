// https://www.acmicpc.net/problem/14003

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector<int> arr;

void print_path(vector<int>& path, int idx) {
	if (path[idx] == idx) {
		cout << arr[idx] << " ";
	}
	else {
		print_path(path, path[idx]);
		cout << arr[idx] << " ";
	}
}

void solution() {
	vector<int> lis;		// lis[k] = 길이가 k인 LIS의 마지막 값
	vector<int> idx;		// idx[k] = 길이가 k인 LIS의 마지막 값의 인덱스
	vector<int> path(n, 0); // path[k] = arr[k]가 포함된 LIS에서 arr[k] 앞의 인덱스

	lis.push_back(arr[0]);
	idx.push_back(0);

	for (int i = 1; i < n; i++) {

		if (lis.back() < arr[i]) {
			path[i] = idx.back();
			lis.push_back(arr[i]);
			idx.push_back(i);
		}
		else { 
			int j = lower_bound(lis.begin(), lis.end(), arr[i]) - lis.begin();

			lis[j] = arr[i];
			idx[j] = i;
			path[i] = j == 0 ? i : idx[j - 1];
		}
	}

	cout << lis.size() << endl;		// LIS의 길이
	print_path(path, idx.back());	// LIS의 원소
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

	solution();

	return 0;
}