// https://programmers.co.kr/learn/courses/30/lessons/12899


const solution = (n) => {
    let answer = [];
    
    while(0 < n) {
        if (n%3 === 0) {
            answer.push(4);
            n = n/3-1;
        }
        else {
            answer.push(n%3);
            n = Math.floor(n/3);
        }
    } 

    return answer.reverse().join('');
}