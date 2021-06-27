#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


void solution(int n) {
	vector<bool> is_prime(n + 1, true);
	vector<int> primes;

	for (int i = 2; i <= (sqrt(n)); i++)
		if (is_prime[i]) {
			int j = i + i;

			while (j <= n) {
				is_prime[j] = false;
				j += i;
			}
		}

	for (int i = 2; i <= n; i++)
		if (is_prime[i])
			primes.push_back(i);

	int result = 0, sum = 0, lo = 0, hi = 0;

	while (1) {
		if (sum >= n) {
			sum -= primes[lo++];
		}
		else if (hi == primes.size()) {
			break;
		}
		else {
			sum += primes[hi++];
		}

		if (sum == n) result++;
	}

	cout << result << endl;
}

int main() {
	int n;
	cin >> n;

	solution(n);

	return 0;
}