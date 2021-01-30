// https://programmers.co.kr/learn/courses/30/lessons/12927


function solution(n, works) {
	let i = 0;
	
	works.sort((a, b) => b - a);
	
	while (n) {
		if (i < works.length-1 && works[i] < works[i+1]) {
			i++;
			continue;
		}
		else if (0 < i && works[i] === works[i-1]) {
			i = 0;
			continue;
		}
	
		works[i] -= 1;
		n--;
	}
	
	return works.reduce((acc, e) => acc + e*e, 0);
}