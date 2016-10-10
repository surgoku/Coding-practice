package DataStructures;

public class BSTNode {
	int data;
	BSTNode left;
	BSTNode right;
	
	public BSTNode(int data){
		this.data = data;
		this.left = null;
		this.right = null;
	}
	
	public void insert(BSTNode root, int val){
		if (root == null){
			root = new BSTNode(val);
			return;
		}
		
		BSTNode current = root;
		BSTNode parent = null;
		
		BSTNode entry = new BSTNode(val);
		
		while (true){
			parent = current;
			if (val < current.data){
				current = current.left;
				if (current == null){
					parent.left = entry;
					return;
				}
			}else{
				current = current.right;
				if (current ==  null){
					parent.right = entry;
					return;
				}
			}
		}
			
	}
	
	

	
}
