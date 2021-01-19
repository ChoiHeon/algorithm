// https://programmers.co.kr/learn/courses/30/lessons/42628



const solution = (operations) => {
    let arr = [];
	
	for (let op of operations) {
		if (op[0] === 'I') {
			arr.push(parseInt(op.slice(2)));
			arr.sort((x, y) => x - y);
		}
		else if (arr.length) {
			if (op[2] == '-')
				arr.shift();
			else
				arr.pop();
		}
	}
	
	return arr.length ? [arr[arr.length-1], arr[0]] : [0, 0];
}