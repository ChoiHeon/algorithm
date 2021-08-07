// 문제: https://www.acmicpc.net/problem/2357

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

const int MAX_N = 100000;
const int LOG_N = 17; // 17 = ceil(log2(MAX_N))
const int MAX_TREE_SIZE = (1 << (LOG_N + 1)) + 1;

int n;
int arr[MAX_N];
int min_tree[MAX_TREE_SIZE];
int max_tree[MAX_TREE_SIZE];

inline int min(int a, int b) { return a < b ? a : b; }
inline int max(int a, int b) { return a > b ? a : b; }

void init(int node, int left, int right) {
	if (left == right) {
		min_tree[node] = arr[left];
		max_tree[node] = arr[left];
		return;
	}

	int mid = (left + right) / 2;

	init(node * 2, left, mid);
	init(node * 2 + 1, mid + 1, right);

	min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1]);
	max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1]);
}

void find(int node, int left, int right, int a, int b, int& min_value, int& max_value) {
	if (b < left || right < a)
		return;
	
	if (a <= left && right <= b) {
		min_value = min(min_value, min_tree[node]);
		max_value = max(max_value, max_tree[node]);
		return;
	}

	int mid = (left + right) / 2;

	find(node * 2, left, mid, a, b, min_value, max_value);
	find(node * 2 + 1, mid + 1, right, a, b, min_value, max_value);
}

int main() {
	int query;

	scanf("%d %d", &n, &query);

	for (int i = 0; i < n; i++)	
		scanf("%d", &arr[i]);

	init(1, 0, n - 1);

	while (query--) {
		int a, b;
		int min_value = 0x7f7f7f7f;
		int max_value = 0;
		
		scanf("%d %d", &a, &b);
		a--; b--;

		find(1, 0, n - 1, a, b, min_value, max_value);
		printf("%d %d\n", min_value, max_value);
	}
	
	return 0;
}
