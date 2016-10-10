
public class LLNode {
	int val;
	LLNode next;
	
	public LLNode(int num){
		this.val = num;
		this.next = null;
	}
	
	public boolean isEmpty(){
		return (next == null);
	}
}
