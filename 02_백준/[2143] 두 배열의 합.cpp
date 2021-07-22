// https://www.acmicpc.net/problem/2143

#include <iostream>
#include <unordered_map>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	long long answer = 0LL;
	long long t;
	int n, m;
	int a[1000];
	int b[1000];
	long long a_sum[1001] = { 0LL, };	// a의 부분합 [i, j] = a_sum[j+1] - a_sum[i]
	long long b_sum[1001] = { 0LL, };	// b의 부분합 [i, j] = b_sum[j+1] - b_sum[i]
	unordered_map<long long, long long> a_sum_count;
	unordered_map<long long, long long> b_sum_count;

	cin >> t;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		a_sum[i + 1] = a_sum[i] + a[i];
	}

	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> b[i];
		b_sum[i + 1] = b_sum[i] + b[i];
	}

	for (int i = 0; i < n; i++)
		for (int j = i; j < n; j++)
			a_sum_count[a_sum[j + 1] - a_sum[i]]++;

	for (int i = 0; i < m; i++)
		for (int j = i; j < m; j++)
			b_sum_count[b_sum[j + 1] - b_sum[i]]++;

	for (auto pair : a_sum_count)
		answer += pair.second * b_sum_count[t - pair.first];

	cout << answer << endl;

	return 0;
}