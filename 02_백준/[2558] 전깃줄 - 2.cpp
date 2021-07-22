// https://www.acmicpc.net/problem/2568

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> pii;

int main() {

	int n;

	scanf("%d", &n);
	vector<pii> v(n);

	for (int i = 0; i < n; i++)
		scanf("%d %d", &v[i].first, &v[i].second);

	sort(v.begin(), v.end());

	vector<int> lis;
	vector<pii> track;

	for (int i = 0; i < n; i++) {
		if (lis.empty() || lis.back() < v[i].second) {
			track.push_back({ lis.size(), v[i].first });
			lis.push_back(v[i].second);
		}
		else {
			auto itr = lower_bound(lis.begin(), lis.end(), v[i].second);
			*itr = v[i].second;
			track.push_back({ itr - lis.begin(), v[i].first });
		}
	}

	vector<int> answer;
	for (int i = track.size() - 1, j = lis.size() - 1; i >= 0; i--) {
		if (track[i].first == j)
			j--;
		else
			answer.push_back(track[i].second);
	}

	sort(answer.begin(), answer.end());

	printf("%d\n", answer.size());
	for (int e : answer)
		printf("%d\n", e);

	return 0;
}
