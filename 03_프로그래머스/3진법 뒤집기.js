function solution(n) {
    const ternary = []
	
	while (n > 0) {
		ternary.unshift(n % 3)
		n = Math.trunc(n / 3)
	}
	
	return ternary.reduce((acc, x, i) => acc + (x * (Math.pow(3, i))), 0)
}