// https://programmers.co.kr/learn/courses/30/lessons/42861


/*
* 크루스칼 알고리즘
	1. 간선들의 가중치들을 오름차순으로 정렬
	2. 모든 간선을 제거합니다.
	3. 가중치가 가장 작은 간선을 생성하는 두 정점이 연결되어 있지 않다면 간선을 생성합니다.
*/


function find(x, parents) {
	if (x === parents[x])
		return x;
	parents[x] = find(parents[x], parents);
	return parents[x];
}

function union(x, y, parents) {
	x = find(x, parents);
	y = find(y, parents);
	
	if (x > y)
		parents[x] = y;
	else
		parents[y] = x;
}

function solution(n, costs) {
	let answer = 0;
	let edges = []
	let parents = []
	const weights = costs.slice().sort((x, y) => x[2] - y[2]);
	
	for (let i = 0; i < n; i++) 
		parents[i] = i;
	
	for (let weight of weights) {
		let v = weight[0];
		let u = weight[1];
		let cost = weight[2];
        
		if (find(v, parents) !== find(u, parents)) {
			answer += cost;
			union(v, u, parents);
		}
	}
	
	return answer;
}


























