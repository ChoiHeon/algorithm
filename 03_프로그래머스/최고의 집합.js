// https://programmers.co.kr/learn/courses/30/lessons/12938



const solution = (n, s) => {
    if (s/n < 1)
        return [-1];

    let answer = Array(n).fill(Math.floor(s/n));

    for (let i = 0; i < s%n; i++)
        answer[n-i-1] += 1;

    return answer;
}