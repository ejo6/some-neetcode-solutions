class Solution {
public:
    int calPoints(std::vector<std::string>& operations) {
        std::vector<int> s;
        
        for (const std::string& op : operations) {
            if (op == "+") {
                // Sum the last two scores
                s.push_back(s[s.size() - 1] + s[s.size() - 2]);
            } else if (op == "D") {
                // Double the last score
                s.push_back(s[s.size() - 1] * 2);
            } else if (op == "C") {
                // Remove the last score
                s.pop_back();
            } else {
                // Convert string to integer and push
                s.push_back(std::stoi(op));
            }
        }
        
        // Sum up all elements in the vector
        int sum = 0;
        for (const int i : s) {
            sum += i;
        } return sum;
    }
};