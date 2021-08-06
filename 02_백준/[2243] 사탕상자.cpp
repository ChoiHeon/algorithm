// 문제: https://www.acmicpc.net/problem/2243

#include <iostream>

using namespace std;

class Candy {
public:
	int sug;
	int cnt;
	int left_cnt = 0;
	int right_cnt = 0;
	Candy* left = nullptr;
	Candy* right = nullptr;

	Candy(int _sug, int _cnt) : sug(_sug), cnt(_cnt) { }
};


int find(Candy* node, int order) {
	pair<int, int> range = { node->left_cnt + 1, node->left_cnt + node->cnt };
	
	if (order < range.first) {
		node->left_cnt--;
		return find(node->left, order);
	}
	else if (range.second < order) {
		node->right_cnt--;
		return find(node->right, order - range.second);
	}
	else {
		node->cnt--;
		return node->sug;
	}
}

Candy* insert(Candy* node, int sug, int cnt) {
	if (node == nullptr) 
		return new Candy(sug, cnt);
	
	if (node->sug == sug) {
		node->cnt += cnt;
	}
	else if (node->sug > sug) {
		node->left_cnt += cnt;
		node->left = insert(node->left, sug, cnt);
	}
	else {
		node->right_cnt += cnt;
		node->right = insert(node->right, sug, cnt);
	}

	return node;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n;
	int a, b, c;
	Candy* root = nullptr;
	
	cin >> n;

	while (n--) {
		cin >> a;

		if (a == 1) {
			cin >> b;
			cout << find(root, b) << "\n";
		}
		else {
			cin >> b >> c;
			root = insert(root, b, c);
		}
	}

	return 0;
}
