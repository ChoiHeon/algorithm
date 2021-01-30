// https://programmers.co.kr/learn/courses/30/lessons/43238


const solution = (n, times) => {
	let copiedTimes = times.slice();
	let low, mid, high;
	let count;
	let answer;
	
	copiedTimes.sort((x, y) => x - y);
	low = 1;
	high = copiedTimes[copiedTimes.length - 1] * n;
	answer = high;
	
	while (low < high) {
		mid = Math.floor((low + high) / 2);
		count = 0;
		
		for (let i = 0; i < copiedTimes.length; i++) {
			count += Math.floor(mid / copiedTimes[i]);
			
                if (n <= count) {
				answer = Math.min(answer, mid);
				break;
			}
		}
		
		if (n <= count)
			high = mid;
		else
			low = mid + 1;
	}
	
	return answer;
}






















