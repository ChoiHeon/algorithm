// https://programmers.co.kr/learn/courses/30/lessons/42586


function solution(progresses, speeds) {
    let works = [];
	let answer = [];
	
    for (let i = 0; i < progresses.length; i++)
        works.unshift((Math.ceil((100 - progresses[i]) / speeds[i])));

    while (works.length > 0) {
        let work = works.pop();
        answer.push(1);

        while (works.length > 0) {
            if (work < works[works.length-1])
                break
            works.pop();
            answer[answer.length-1] += 1;
        }
    }

    return answer;
}