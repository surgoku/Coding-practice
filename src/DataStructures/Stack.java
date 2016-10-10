package DataStructures;

public class Stack {
	Node top;
	
	void push(int item){
		
		Node newTop = new Node(item);
		newTop.next = top;
		top = newTop;
	}
	
	Node pop(){
		if (top != null){
			int toReturnVal = top.data;
			top = top.next;
			Node toReturn = new Node(toReturnVal);
			return toReturn;
		}
		return null;
	}
}
