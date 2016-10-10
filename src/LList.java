import java.util.HashSet;


public class LList {

	public static LLNode deleteDups(LLNode root){
		HashSet<Integer> set = new HashSet<Integer>();
		LLNode revisedList = null;
		
		LLNode previousNode = null;
		if (root != null){
			revisedList = new LLNode(root.val);
			set.add(root.val);
			root = root.next;
			if (root != null){
				previousNode = root;
				revisedList.next = previousNode;
				set.add(root.val);
			}
		}
		while (root.next != null){
			if (set.contains(root.val)){
				previousNode.next = root.next;
			}else{
				set.add(root.val);
				previousNode = root;
			}
			
			root = root.next;
		}
		return revisedList;
		
	}
	
	
	public static void printKToEnd(LLNode root, int k){
		LLNode firstNode = root;
		LLNode leadingNode = root;
		
		if (k<0 || root == null){
			return;
		}
		
		for (int i=0; i <k; i++){
			if (leadingNode == null) return;
			leadingNode = leadingNode.next;
		}
		
		if (leadingNode == null) return;
		
		while(leadingNode !=null){
			leadingNode = leadingNode.next;
			firstNode = firstNode.next;
		}
		
		while(firstNode != null){
			System.out.println(firstNode.val);
			firstNode = firstNode.next;
		}

	}
	
	public static int getSizeLL(LLNode root){
		if (root == null) return 0;
		int count = 0;
		while (root != null){
			count += 1;
			root = root.next;
		}
		return count;
	}
	
	public static LLNode addLL(LLNode root1, LLNode root2, int carry){
		
		if (getSizeLL(root1) != getSizeLL(root2)){
			System.out.println("different size");
			return null;
		}
		
		if (root1 == null || root2 == null ) {
			if (carry ==0) return null;
		}
		
		int val = carry;
		
		LLNode out = new LLNode(carry);
		
		if (root1 != null) val += root1.val;
		if (root2 != null) val += root2.val;
		
		out.val = val %10;
		
		if (root1 != null || root2 != null ){
			LLNode res = addLL(root1 == null ? null : root1.next, root2 == null ? null: root2.next, val>=10? 1:0);
			out.next = res;
		}

		return out;
	}
	
	public static LLNode returnNodeAtBeginningOfLoop(LLNode root){
		
		LLNode slow = root;
		LLNode fast = root;
		
		// both meet but does not imply that the beginning of loop
		while (fast !=null && fast.next != null){
			slow = slow.next;
			fast = fast.next.next;
			if (slow == fast){
				return slow;
			}
		}
		
		// edge case no loop
		if (fast == null || fast.next == null){
			return null;
		}
		
		// finding loop beginning: from the matching point. Beginning of loop is actually k steps ahead of the meeting point.
		// where k is the distance of the loop from the beginning. if k==0, then the meeting point itself is the beginning of loop
		
		slow = fast;
		while(slow != fast){
			slow = slow.next;
			fast = fast.next;
		}
		
		return slow;
	}
	
	public static boolean isPalindrome(LLNode root){
		Stack stack = new Stack();
		
		LLNode fast = root;
		LLNode slow = root;
		
		while(fast != null || fast.next != null){
			stack.push(slow.val);
			slow = slow.next;
			fast = fast.next.next;
		}
		
		// odd number of elements
		if(fast !=null){
			slow = slow.next;
		}
		
		while(slow !=null){
			if (slow.val == stack.pop().data){
				continue;
			}else{
				return false;
			}
		}
		
		
		return true;
	}
	
	public static void printLL(LLNode root){
		while(root != null){
			System.out.println(root.val);
			root = root.next;
		}
	}
	
	
	public static void main(String[] args){
		LLNode root = new LLNode(5);
		LLNode node = new LLNode(4);
		root.next = node;
		node = new LLNode(3);
		root.next.next = node;
		node = new LLNode(3);
		root.next.next.next = node;
		node = new LLNode(4);
		root.next.next.next.next = node;
		node = new LLNode(5);
		root.next.next.next.next.next = node;
		node = new LLNode(6);
		root.next.next.next.next.next.next = node;
		
		
		LLNode root2 = new LLNode(11);
		node = new LLNode(21);
		root2.next = node;
		node = new LLNode(31);
		root2.next.next = node;
		node = new LLNode(31);
		root2.next.next.next = node;
		node = new LLNode(41);
		root2.next.next.next.next = node;
		node = new LLNode(51);
		root2.next.next.next.next.next = node;
		node = new LLNode(61);
		root2.next.next.next.next.next.next = node;
		//LLNode uniqueElemList = deleteDups(root);
		//printLL(uniqueElemList);
		//printKToEnd( root, 5);
		
		//LLNode sumOfLL = addLL(root, root2, 0);
		//printLL(sumOfLL);
		
	}
	
}
