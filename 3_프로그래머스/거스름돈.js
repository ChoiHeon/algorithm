// https://programmers.co.kr/learn/courses/30/lessons/12907


function solution(n, money) {
    const m = money.length;
    let dp = Array.from(Array(m+1), () => Array(n+1))

    dp.forEach((e, i) => {
        dp[i].fill(0);
        dp[i][0] = 1;
    });

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            dp[i][j] += dp[i-1][j];

            if (money[i-1] <= j )
                dp[i][j] += dp[i][j-money[i-1]];
        }
    }
    return dp[m][n];
}
