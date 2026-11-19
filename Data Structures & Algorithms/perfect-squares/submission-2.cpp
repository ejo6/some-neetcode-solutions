class Solution {
public:
    int numSquares(int n) {
        std::vector<int> dp(n + 1, 10001);
        dp[0] = 0;

        std::vector<int> squares;
        int i = 1;
        while (i * i <= n) {
            squares.push_back(i * i);
            i++;
        }

        for (int square : squares) {
            for (int j = square; j <= n; j++) {
                dp[j] = std::min(dp[j - square] + 1, dp[j]);
            }
        }

        return dp[n];
    }
};