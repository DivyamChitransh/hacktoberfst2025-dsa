# You are given a 2D grid of size n × m, where each cell contains a non-negative integer. Starting from the top-left cell (0, 0), your goal is to reach the bottom-right cell (n-1, m-1).

# At each step, you can only move either right or down.

# Your task is to determine the minimum possible sum of the values along any valid path from the top-left to the bottom-right corner.





def minPathSum(grid):
    n,m=len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[n-1][m-1]
