class Solution {

    std::string s;

    private:
        bool isPalindrome(int l, int r) {
            while (l < r) {
                if (s[l] != s[r]) {
                    return false;
                } l++, r--;
            } return true;
        }

    public:
        bool validPalindrome(string s) {
            this->s = s;

            int l = 0, r = s.size() - 1;
            while (l < r) {
                if (s[l] != s[r]) {
                    return (isPalindrome(l + 1, r) or isPalindrome(l, r - 1));
                } l++, r--;
            } return true;
        }
};