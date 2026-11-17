class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int best = 0, curr = 0;
        for (auto num : nums) {
            if (num == 1) {
                curr++;
                best = std::max(best, curr);
            } else {
                curr = 0;
            }
        }

        return best;
    }
};