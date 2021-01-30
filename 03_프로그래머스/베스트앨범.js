// https://programmers.co.kr/learn/courses/30/lessons/42579


function solution(genres, plays) {
	let n = genres.length;
	let indexByGenre = new Map();
	let totalPlayByGenre
	let answer = [];
	
	for (let i = 0; i < n; i++) 
		if (!indexByGenre.has(genres[i])) 
			indexByGenre.set(genres[i], [i]);
		else 
			indexByGenre.set(genres[i], indexByGenre.get(genres[i]).concat(i));
	
	totalPlayByGenre = [...indexByGenre].map(x => [x[0], x[1].reduce((acc, x) => acc + plays[x], 0)]);
    totalPlayByGenre.sort((a, b) => b[1] - a[1]);
	
	for (let pair of totalPlayByGenre) {
		let genre = pair[0];
		let indexList = indexByGenre.get(genre);
		indexList.sort((a, b) => plays[b] - plays[a]);
		
		answer.push(indexList[0], indexList[1]);
	}
	
	return answer;
}