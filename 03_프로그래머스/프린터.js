// https://programmers.co.kr/learn/courses/30/lessons/42587


/*
1. Map 객체에 우선순위-개수 쌍을 저장한다.
2. 우선순위들의 중복을 제거한 뒤, 오름차순으로 정렬한다. (orders)
3. priorities의 첫번째 원소를 shift.
4-1. 첫번째 원소가 가장 큰 우선순위일 경우, answer에 push.
4-1-1. Map 객체에서 키가 첫번째 원소의 개수가 0이라면, orders에서 제거한다.
4-2. 해당 원소보다 큰 우선순위가 있을 경우, priorities에 push.

*/


function solution(priorities, location) {
    let dict = new Map();
    let orders = [...new Set(priorities)].sort();
    let pairs = priorities.map((e, i) => [e, i]);

    let answer = 0;
    let pair;

    for (let p of priorities) {
        if (!dict.has(p))
            dict.set(p, 1)
        else
            dict.set(p, dict.get(p)+1)
    }

    while (true) {
        pair = pairs.shift();

        if (pair[0] === orders[orders.length-1]) {
            answer += 1;

            if (pair[1] === location)
                return answer;

            dict.set(pair[0], dict.get(pair[0])-1);

            if (dict.get(pair[0]) === 0)
                orders.pop();
        }
        else
            pairs.push(pair);
    }

    return answer[location];
}
