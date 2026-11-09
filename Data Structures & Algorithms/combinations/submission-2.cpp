class Solution {
    int n, k;
    std::vector<std::vector<int>> result;
    std::vector<int> curr;

private:
    void backtrack(int i) {
        // Base case 1:
        if (curr.size() == k) {
            result.push_back(curr);
            return;
        }
        // Base case 2:
        if (n - i + 1 + curr.size() < k) {
            return;
        } 
        // Case 1:
        curr.push_back(i);
        backtrack(i + 1);
        // Case 2:
        curr.pop_back();
        backtrack(i + 1);
    }
        
public:
    vector<vector<int>> combine(int n, int k) {
        this->k = k;
        this->n = n;
        backtrack(1);
        return result;
    }
};

        // All possible combinations of k numbers from 1-n
        // Backtracking (no shortcuts here):
        // Num combinations: nCk? = n!/k!(n-k)!
        // We need to make include everyone of these, so 
        // Time is O(k * n!/k!(n-k)!)
        //   -> k inserts on nCk possibilities 
        // Space is O(k * n!/k!(n-k)! + n)
        //   -> k elements on nCk possibilies plus max recusion depth of n

        // Imagine a list of numbers 1-n, for each combination (curr):
        //   Case 1: Include the number
        //   Case 2: Don't include the number
        //   Base case 1: Size of curr is k, curr to result
        //   Base case 2: we cannot make k with the remaining elements
        // return result

        // Recurse this until no calls are left

        // For C++, not bothering with lambda, declaring n, k, result, curr 
        // as fields in the class




