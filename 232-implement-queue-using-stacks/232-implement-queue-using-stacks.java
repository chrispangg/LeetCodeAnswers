import java.util.ArrayList;
class MyQueue {
    ArrayList<Integer> stack;

    public MyQueue() {
        stack = new ArrayList<Integer>();
       
    }

    public void push(int x) {
        stack.add(x);
    }

    public int pop() {
        int value = stack.get(0);
        int nextNode;
        for (int i = 0; i < stack.size() - 1; i++) {
            nextNode = stack.get(i + 1);
            stack.set(i, nextNode);
        }
        stack.remove(stack.size()-1);
        return value;
    }

    public int peek() {
        return stack.get(0);
    }

    public boolean empty() {
        boolean val = false;
        if(stack.size() == 0){
            val = true;
        }
        return val;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */