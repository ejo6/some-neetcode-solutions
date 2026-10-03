class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> parentheses = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        parentheses.put('}', '{');
        parentheses.put(']', '[');
        parentheses.put(')', '(');

        for (char i : s.toCharArray()) {
            if (parentheses.containsValue(i)) {
                stack.push(i);
            } else {
                if (stack.isEmpty()) return false;
                else if (parentheses.get(i) == stack.peek()) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.size() == 0;
    }
}