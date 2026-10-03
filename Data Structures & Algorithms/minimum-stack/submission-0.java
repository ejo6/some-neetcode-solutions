class MinStack {

    private int[] arr;
    private int capacity;
    private int top; // index of top element
    private int[] minArr;

    public MinStack() {
        capacity = 10;
        arr = new int[capacity];
        minArr = new int[capacity];
        top = -1;
    }
    
    private void ensureCapacity() {
        if (top + 1 == capacity) {
            int newCapacity = capacity + 10;
            int[] newArr = new int[newCapacity];
            int[] newMinArr = new int[newCapacity];

            for (int i = 0; i < capacity; i++) {
                newArr[i] = arr[i];
            }

            for (int i = 0; i < capacity; i++) {
                newMinArr[i] = minArr[i];
            }

            arr = newArr;
            minArr = newMinArr;
            capacity = newCapacity;
        }
    }

    public void push(int val) {
        ensureCapacity();
        top++;

        arr[top] = val;
        if (top == 0) {
            minArr[top] = val;
        } else {
            minArr[top] = Math.min(val, minArr[top - 1]);
        }
    }
    
    public void pop() {
        top--; // dont technically need to erase
    }
    
    public int top() {
        return arr[top];
    }
    
    public int getMin() {
        return minArr[top];
    }
}
