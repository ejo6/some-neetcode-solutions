class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        std::vector<vector<int>> pascals = {{1}};

        for (int i = 1; i < numRows; i++) {
            std::vector<int> curr;
            for (int j = 0; j < i + 1; j++) {
                int v1 = (j - 1 < 0) ? 0 : pascals[i - 1][j - 1];
                int v2 = (j > i - 1) ? 0 : pascals[i - 1][j];

                curr.push_back(v1 + v2);
            }
            pascals.push_back(curr);
        }
        return pascals;
    }
};