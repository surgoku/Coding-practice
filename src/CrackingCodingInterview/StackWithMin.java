package CrackingCodingInterview;

import java.util.Stack;

public class StackWithMin extends Stack<Integer> {
	
	//Stack<Integer> s;
	private Stack<Integer> minS;
	
	public StackWithMin(){
		//s = new Stack<Integer>();
		minS = new Stack<Integer>();
	}
	
	public Integer pop(){
		int val = super.pop();
		if (val == minS.peek()){
			minS.pop();
		}
		
		return val;
	}
	
	public void push(int val){
		if (val < min()){
			minS.push(val);
		}	
		super.push(val);	
	}
	
	public int min(){
		if (minS.isEmpty()){
			return Integer.MAX_VALUE;
		}else{
			return minS.peek();
		}
	}
	

}
