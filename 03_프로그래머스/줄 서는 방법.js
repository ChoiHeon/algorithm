// https://programmers.co.kr/learn/courses/30/lessons/12936


const solution = (n, k) => {
    let numbers = Array(n).fill(null).map((x, i) => i+1);
    let factorials = [1];
    let answer = [];

    for (let i = 1; i < 20; i++)
        factorials[i] = factorials[i-1] * i;

    k -= 1;

    for (let i = n-1; i > 0; i--) {
        let p = Math.floor(k / factorials[i]);
        console.log(p);
        answer.push(numbers[p]);
        numbers.splice(p, 1);
        k = k % factorials[i];
    }

    return answer.concat(numbers);
}


// 테스트 코드
console.log(solution(4, 24));   // expected output: [4, 3, 2, 1]