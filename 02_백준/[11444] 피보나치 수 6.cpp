// https://www.acmicpc.net/problem/11444


#include <iostream>

using namespace std;

typedef long long ll;

const ll BOUND = 1000000007LL;

struct Matrix2x1 {
public:
	ll a11, a21;

	Matrix2x1(ll _a11, ll _a21) : a11(_a11), a21(_a21) { }
	Matrix2x1& operator= (const Matrix2x1& rhs);
};

Matrix2x1& Matrix2x1::operator= (const Matrix2x1& rhs) {
	a11 = rhs.a11;
	a21 = rhs.a21;

	return *this;
}


struct Matrix2x2 {
public:
	ll a11, a12, a21, a22;

	Matrix2x2() : a11(0), a12(0), a21(0), a22(0) { }
	Matrix2x2 (ll _a11, ll _a12, ll _a21, ll _a22) : a11(_a11), a12(_a12), a21(_a21), a22(_a22) { }
	Matrix2x2(const Matrix2x2& rhs) : a11(rhs.a11), a12(rhs.a12), a21(rhs.a21), a22(rhs.a22) { }
	Matrix2x2& operator= (const Matrix2x2&& rhs);
	Matrix2x2 operator* (const Matrix2x2& rhs) const;
	Matrix2x1 operator* (const Matrix2x1& rhs) const;
};

Matrix2x2& Matrix2x2::operator= (const Matrix2x2&& rhs) {
	a11 = rhs.a11;
	a12 = rhs.a12;
	a21 = rhs.a21;
	a22 = rhs.a22;

	return *this;
}

Matrix2x2 Matrix2x2::operator* (const Matrix2x2& rhs) const {
	return Matrix2x2(((a11*rhs.a11) % BOUND + (a12*rhs.a21) % BOUND) % BOUND, ((a11*rhs.a12) % BOUND + (a12*rhs.a22) % BOUND) % BOUND,
					 ((a21*rhs.a11) % BOUND + (a22*rhs.a21) % BOUND) % BOUND, ((a21*rhs.a12) % BOUND + (a22*rhs.a22) % BOUND) % BOUND);
}

Matrix2x1 Matrix2x2::operator* (const Matrix2x1& rhs) const {
	return Matrix2x1(((a11*rhs.a11) % BOUND + (a12*rhs.a21) % BOUND) % BOUND, 
		             ((a21*rhs.a11) % BOUND + (a22*rhs.a21) % BOUND) % BOUND);
}

ll solution(long long n) {
	Matrix2x1 g(0, 1);
	Matrix2x2 M[100];

	M[0] = Matrix2x2(0, 1, 1, 1);

	for (int i = 1; i < 100; i++)
		M[i] = M[i-1] * M[i-1];

	int x = 0;
	Matrix2x2 A(1, 0, 0, 1);

	while (n) {
		if (n & 1)
			A = A * M[x];

		n /= 2;
		++x;
	}

	g = A * g;
	
	return g.a11;
}


int main() {
	
	ll n, answer;

	cin >> n;

	answer = solution(n);

	cout << answer << endl;

	return 0;
}