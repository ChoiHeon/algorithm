// https://programmers.co.kr/learn/courses/30/lessons/12923



const solution = (begin, end) => {
	let answer = [];
	
	for (let i = begin; i <= end; i++) {
		if (i < 2)
			answer.push(0);
		else {
			let flag = false;
			for (let j = 2; j < Math.floor(Math.sqrt(i)) + 1; j++)
				if (i % j === 0 && i / j <= 10000000) {
					answer.push(i / j);
					flag = true;
					break;
				}
			if (!flag)
				answer.push(1)
		}
	}
	
	return answer;
}