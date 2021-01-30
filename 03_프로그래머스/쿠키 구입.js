// https://programmers.co.kr/learn/courses/30/lessons/49995



const solution = (cookies) => {
    let answer = 0;
    
    for (let i = 0; i < cookies.length-1; i++) {
        let left = i;
        let right = i+1;
        let leftSum = cookies[left];
        let rightSum = cookies[right];

        while(true) {
            if (leftSum === rightSum && answer < leftSum) {
                answer = leftSum;
            }
            else if (leftSum <= rightSum && 0 < left) {
                left--;
                leftSum += cookies[left];
            }
            else if (leftSum > rightSum && right < cookies.length ) {
                right++;
                rightSum += cookies[right];
            }
            else {
                break;
            }
        }
    }

    return answer;
}
