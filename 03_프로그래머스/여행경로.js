// https://programmers.co.kr/learn/courses/30/lessons/43164


const solution = (tickets) => {
	let answer = [];
	
	const dfs = (country, path, tickets) => {
		let newPath = [...path, country];
		
		if (tickets.length === 0)
			answer.push(newPath);
		else {
			tickets.map((ticket, i) => {
				if (country === ticket[0]) {
					let newTickets = tickets.map((x, i) => [...x]);
					newTickets.splice(i, 1);
					dfs(ticket[1], newPath, newTickets);
				}
			})
		}
	}

	dfs("ICN", [], tickets);
	return answer.sort()[0];
}