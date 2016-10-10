package CrackingCodingInterview;

import java.util.Stack;


public class StackChapter3 {
	
	public static Stack<Integer> towerOfHanoiRecur(int n, Stack<Integer> source, Stack<Integer> destination, Stack<Integer> buffer){
		if (n > 0){
			
			buffer = towerOfHanoiRecur(n-1, source, buffer, destination);
			destination.add(n);
			source.pop();
			//System.out.println(n);
			destination = towerOfHanoiRecur(n-1,buffer, destination, source);
			return destination;
			
		}else if (n==0){ 
			return destination;
		}else{
			return null;
		}
		
		
		//return null;
	}
	
	public static void main(String[] args){
		Stack<Integer> stack1 = new Stack<Integer>();
		Stack<Integer> stack2 = new Stack<Integer>();
		Stack<Integer> stack3 = new Stack<Integer>();
		
		stack1.add(4);
		stack1.add(3);
		stack1.add(2);
		stack1.add(1);
		
		stack1 = towerOfHanoiRecur(4, stack1, stack2, stack3);
		while(!stack1.isEmpty()){
			System.out.println(stack1.pop());
		}
		
		/*
		StackWithMin sMin = new StackWithMin();
		sMin.push(1000);
		sMin.push(-2);
		sMin.push(10);
		sMin.push(4);
		sMin.push(0);
		sMin.push(-10);
		sMin.push(-100);
		while(!sMin.isEmpty()){
			System.out.println(sMin.min());
			System.out.println(sMin.pop());
		}
		*/
		
		
		
		
	}
}



