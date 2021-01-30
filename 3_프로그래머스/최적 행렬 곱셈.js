// https://programmers.co.kr/learn/courses/30/lessons/12942

/*
dp[i][i] = 0
dp[i][j] = max(d[i][k] + (p[i][0] * p[k][1] * p[j][1]) + dp[k+1][j])    (i < j && i <= k < j)
*/

const solution = (matrix) => {
    let dp = Array.from(Array(matrix.length), () => Array(matrix.length));
    dp.forEach((e, i) => {
        dp[i].fill(Infinity);
        dp[i][i] = 0;
    });

    for (let t = 1; t < matrix.length; t++) {
        for (let i = 0; i < matrix.length-t; i++) {
            let j = i+t;
            for (let k = i; k < j; k++) {
                dp[i][j] = Math.min(dp[i][j], dp[i][k] + (matrix[i][0] * matrix[k][1] * matrix[j][1]) + dp[k+1][j]);
            }
        }
    }

    return dp[0][matrix.length-1];
}
