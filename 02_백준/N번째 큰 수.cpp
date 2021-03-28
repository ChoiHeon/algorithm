// https://www.acmicpc.net/problem/2693


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int solution(vector<int> arr) {
	int result = -1;



	return result;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); 
	cout.tie(NULL);

	int t = -1;
	vector<int> arr(10);
	cin >> t;
	
	for (int i = 0; i < t; i++) {
		for (int i = 0; i < 10; i++) 
			cin >> arr[i];
		cout << solution(arr) << endl;
	}
}
