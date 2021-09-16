// https://www.acmicpc.net/problem/3653

#include <iostream>
#include <vector>

using namespace std;

struct Segment {
	int size;
	vector<int> tree, idx;

	Segment(int N, int M) {
		size = N + M;
		idx.resize(N);
		tree.resize(4 * size, 0);
	}

	int init(int node, int M, int left, int right) {
		if (left == right) {
			if (left >= M) {
				idx[left - M] = left;
				tree[node] = 1;
			}

			return tree[node];
		}

		int mid = (left + right) / 2;
		return tree[node] = init(node * 2, M, left, mid) + init(node * 2 + 1, M, mid + 1, right);
	}

	void init(int M) {
		init(1, M, 0, size - 1);
	}

	int query(int node, int left, int right, int nL, int nR) {

		if (right < nL || left > nR)
			return 0;
		if (left <= nL && nR <= right)
			return tree[node];

		int mid = (nL + nR) / 2;

		return query(node * 2, left, right, nL, mid) + query(node * 2 + 1, left, right, mid + 1, nR);

	}


	int query(int left, int right) {
		return query(1, left, idx[right] - 1, 0, size - 1);
	}

	int update(int idx, int node, int val, int nL, int nR) {
		if (idx < nL || nR < idx)
			return tree[node];
		if (nL == nR)
			return tree[node] = val;

		int mid = (nL + nR) / 2;
		return tree[node] = update(idx, node * 2, val, nL, mid) + update(idx, node * 2 + 1, val, mid + 1, nR);
	}

	int update(int index, int val) {
		return update(idx[index], 1, val, 0, size - 1);
	}

	void change(int index, int val) {
		idx[index] = val;
	}
};

int main() {
	int t;
	int n, m;
	int p, q;

	scanf("%d", &t);

	while (t--) {
		scanf("%d %d", &n, &m);

		Segment seg(n, m);
		seg.init(m);
		p = m - 1;

		while (m--) {
			scanf("%d", &q);
			q--;

			printf("%d ", seg.query(0, q));

			seg.update(q, 0);
			seg.change(q, p--);
			seg.update(q, 1);
		}

		printf("\n");
	}

	return 0;
}

