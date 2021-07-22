// https://www.acmicpc.net/problem/5639


#include <iostream>
#include <vector>

using namespace std;


struct Node {
public:
	int value;
	Node* left;
	Node* right;

	Node(int v) : value(v) {
		left = right = NULL;
	}
};

Node* insert(Node* node, int v) {
	if (node == NULL)
		return new Node(v);
	if (node->value > v)
		node->left = insert(node->left, v);
	else
		node->right = insert(node->right, v);

	return node;
}

void post_order(Node* node) {
	if (node == NULL)
		return;
	
	post_order(node->left);
	post_order(node->right);
	cout << node->value << endl;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int v;
	Node* root = NULL;

	while (cin >> v) {
		if (v == EOF) 
			break;
		root = insert(root, v);
	}

	cout << "start post-order" << endl;
	post_order(root);
}