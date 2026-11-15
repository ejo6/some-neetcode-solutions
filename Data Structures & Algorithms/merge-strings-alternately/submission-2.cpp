class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string res;
        res.reserve(word1.size() + word2.size());

        size_t l = std::min(word1.size(), word2.size());

        for (size_t i = 0; i < l; i++) {
            res += (word1[i]);
            res += (word2[i]);
        }

        res += word1.substr(l);
        res += word2.substr(l);

        return res;
    }
};