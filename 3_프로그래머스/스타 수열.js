// https://programmers.co.kr/learn/courses/30/lessons/70130
// 참고: https://hirlawldo.tistory.com/49


function solution(a) {
	let counter = Array(a.length).fill(0);
	let answer = 0;
	
	a.forEach(e => counter[e]++);
    
    counter.forEach((e, i) => {
        if (e <= answer)
            return;
        
        let len = 0;
		
		for (let j = 0; j < a.length-1; j++)
			if ((a[j] === i || a[j+1] === i) && (a[j] !== a[j+1])) {
				len++;
				j++;
			}
        
		answer = Math.max(answer, len);
    });
	
	return answer * 2;
}