// https://programmers.co.kr/learn/courses/30/lessons/49191



function solution(n, results) {
	let players = {};
	let games = {};
	let answer = 0;
	
	for (let i = 0; i < n; i++) 
		games[i] = { win: [], lose: [] };

	results.forEach(result => {
        games[result[0]-1].win.push(result[1]-1);
        games[result[1]-1].lose.push(result[0]-1);
    });
	
	for (let _ = 0; _ < n; _++) {
		for (let i = 0; i < results.length; i++) {
			let winner = results[i][0]-1;
			let loser = results[i][1]-1;
			
			for (let j = 0; j < n; j++) {
				if (games[j].win.length + games[j].lose.length === n-1)
					continue;
					
				if (games[j].win.includes(winner) && !games[j].win.includes(loser))
					games[j].win.push(loser);
				if (games[j].lose.includes(loser) && !games[j].lose.includes(winner))
					games[j].lose.push(winner);
			}
		}
	}
	
	for (let i = 0; i < n; i++)
		if (games[i].win.length + games[i].lose.length === n-1)
			answer++;
    
	return answer;
}






























