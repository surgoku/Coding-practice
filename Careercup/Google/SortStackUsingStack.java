package Google;

import java.util.Stack;

public class SortStackUsingStack {
	
	
	public static Stack<Integer> sortStack(Stack<Integer> s){
		
		Stack<Integer> tempStack = new Stack<Integer>();
		
		while(!s.isEmpty()){
			int temp = s.pop();
			while(!tempStack.isEmpty() && tempStack.peek() > temp){
				s.push(tempStack.pop());
			}
			tempStack.push(temp);
		}
		return tempStack;
		
	}
	
	
	public static void main(String[] args){
		Stack<Integer> input = new Stack<Integer>();
        input.add(34);
        input.add(3);
        input.add(31);
        input.add(98);
        input.add(92);
        input.add(23);
        
        Stack<Integer> output = sortStack(input);
        
        while(!output.isEmpty()){
        	System.out.println(output.pop());
        }
		
	}

}
