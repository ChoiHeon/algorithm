// https://programmers.co.kr/learn/courses/30/lessons/12904


const solution = (s) => {
	let answer = 1;
	let chIdx = {};
	
	for (let i = s.length-1; -1 < i; i--) // 문자별로 인덱스를 내림차순으로 저장
		if (s[i] in chIdx) 
			chIdx[s[i]].push(i);
		else 
			chIdx[s[i]] = [i];
	
	for (let i = 0; i < s.length; i++)
		for (let j of chIdx[s[i]]) { // 첫 문자와 마지막 문자가 같은 범위를 탐색 
			if (j-i < answer) // 탐색하려는 범위가  현재까지 가장 긴 팰린드롬의 길이 이하일 경우, 반복문 종료
				break;
				
			let isPal = true;
			
			for (let k = 0; k < Math.ceil((j-i)/2); k++) // 팰린드롬임을 확인하기 위해 최소 횟수 반복
				if (s[i+k] !== s[j-k]) {
					isPal = false
					break;
				}
			
			if (isPal) // 16번쨰 줄 코드로 인해 위에서 탐색한 팰린드롬이 가장 긴 길이임을 알 수 있다
				answer = j-i+1;
		}
	
	return answer;
}






























