class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int whites = std::count(blocks.begin(), blocks.begin() + k, 'W');
        int best = whites;

        for (size_t r = k; r < blocks.size(); r++) {
            whites += (blocks[r] == 'W');
            whites -= (blocks[r - k] == 'W');
            best = std::min(whites, best);
        } return best;
    }
};