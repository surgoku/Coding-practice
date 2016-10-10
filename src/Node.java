
public class Node {
	int data;
	Node next = null;
	
	public Node(int d){
		this.data = d;
	}
	
	void addToTail(int d){
		Node end = new Node(d);
		Node n = this;
		
		while(n.next != null){
			n = n.next;
		}
		
		n.next = end;
	}
	
}
