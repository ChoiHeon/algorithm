// https://programmers.co.kr/learn/courses/30/lessons/49994


function solution(commands) {
	let pos = [0, 0]
	let loads = new Set();
	const dirs = {'U': [1, 0], 'D': [-1, 0], 'L': [0, -1], 'R': [0, 1]};
	const reverse = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'};
	
	for (let cmd of commands) {
		let next = [pos[0]+dirs[cmd][0], pos[1]+dirs[cmd][1]];
		
		if (next[0] > 5 || next[0] < -5 || next[1] > 5 || next[1] < -5)
			continue;
			
		loads.add(pos+cmd);
		loads.add(next+reverse[cmd]);
		pos = next;
	}
	
	return loads.size / 2;
}