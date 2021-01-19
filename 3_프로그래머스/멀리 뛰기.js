// https://programmers.co.kr/learn/courses/30/lessons/12914


function solution(n) {
	let a = 0;
	let b = 1;
	
	for (let i = 0; i < n; i++) {
		let tmp = b;
		b = (a + b) % 1234567
        a = tmp;
	}
	
	return b;
}