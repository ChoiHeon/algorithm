// 문제: https://www.acmicpc.net/problem/2042

#include <iostream>

using namespace std;
typedef long long ll;

const int MAX_N = 1000000;
const int TREE_SIZE = (1 << (20 + 1)) + 1;

int n, m, k;
ll arr[MAX_N];		// 시작 인덱스 = 0
ll tree[TREE_SIZE];	// 시작 인덱스 = 1


/*
node = 세그먼트 트리의 노드
left, right = 배열의 범위
*/
ll init(int node, int left, int right) {
	if (left == right)
		return tree[node] = arr[left];

	int mid = (left + right) / 2;
	
	return tree[node] = init(node * 2, left, mid) + init(node * 2 + 1, mid + 1, right);
}


/*
node = 세그먼트 트리의 노드
index = 배열의 값을 변경할 인덱스
diff = 기존의 값과 변경할 값의 차이
left = 배열의 범위
*/
void update(int node, int left, int right, int index, ll diff) {
	if (index < left || right < index)
		return;

	tree[node] += diff;

	if (left != right) {
		int mid = (left + right) / 2;
		
		update(node * 2, left, mid, index, diff);
		update(node * 2 + 1, mid + 1, right, index, diff);
	}
}


/*
node = 세그먼트 트리의 노드
left, right = 현재 노드가 가리키는 배열의 범위
start, end = 합을 구하려는 배열의 범위
*/
ll sum(int node, int left, int right, int start, int end) {
	if (end < left || right < start)
		return 0LL;

	if (start <= left && right <= end)
		return tree[node];

	int mid = (left + right) / 2;

	return sum(node * 2, left, mid, start, end) + sum(node * 2 + 1, mid + 1, right, start, end);
}

void print() {
	for (int i = 0; i < 13; i++)
		cout << tree[i] << " ";
	cout << endl;
}

int main() {
	scanf("%d %d %d", &n, &m, &k);

	for (int i = 0; i < n; i++) 
		scanf("%lld", &arr[i]);

	init(1, 0, n - 1);

	int t = m + k;
	int a, b;
	ll c;

	while (t--) {
		scanf("%d %d %lld", &a, &b, &c);

		if (a == 1) {
			update(1, 0, n - 1, b - 1, c - arr[b - 1]);
			arr[b - 1] = c;
		}
		else
			printf("%lld\n", sum(1, 0, n - 1, b - 1, c - 1));
	}

	return 0;
}