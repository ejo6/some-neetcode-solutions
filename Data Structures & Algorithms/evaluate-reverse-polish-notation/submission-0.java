class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String t : tokens) {
            if (t.equals("+") || t.equals("-") || t.equals("*") || t.equals("/")) {
                if (t.equals("+")) {
                    int op1 = stack.pop();
                    int op2 = stack.pop();
                    System.out.println(op2 + " + " + op1);
                    stack.push(op2 + op1);
                } else if (t.equals("-")) {
                    int op1 = stack.pop();
                    int op2 = stack.pop();
                    System.out.println(op2 + " - " + op1);
                    stack.push(op2 - op1);
                } else if (t.equals("*")) {
                    int op1 = stack.pop();
                    int op2 = stack.pop();
                    System.out.println(op2 + " * " + op1);
                    stack.push(op2 * op1);
                } else {
                    int op1 = stack.pop();
                    int op2 = stack.pop();
                    System.out.println(op2 + " / " + op1);
                    stack.push(op2 / op1);
                }
            } else {
                stack.push(Integer.parseInt(t));
            }
            System.out.println(stack.peek());
        }

        return stack.pop();
        
    }
}
