
public class Queue {
	
	Node first, last;
	
	void enqueue(int item){
		
		if (first == null){
			first = new Node(item);
			last = first;
		}else{
			Node toAdd = new Node(item);
			last.next = toAdd;
			last = toAdd;
		}
	}
	
	Node dequeue(){
		if (first == null){
			return null;
		}else{
			Node toReturn = new Node(first.data);
			first = first.next;
			return toReturn;
		}
	}
}
