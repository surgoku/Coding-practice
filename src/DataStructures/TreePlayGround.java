package DataStructures;

import java.util.ArrayList;
import java.util.LinkedList;

public class TreePlayGround {
	
	
	
	public static boolean bfs(TreeNode root, int val){
		if (root == null) return false;
		
		LinkedList<TreeNode> q = new LinkedList<TreeNode>();
		
		q.add(root);
		
		while (!q.isEmpty()){
			TreeNode node = q.poll();
			if (node.data == val) return true;
			if (node.left != null) q.add(node.left);
			if (node.right != null) q.add(node.right);
			
		}
		
		return false;
	}
	
	public static boolean dfsRecur(TreeNode root, int val){
		if (root == null) {
			return false;
		} else if (root.data == val) {
			return true;
		}else{
			return dfsRecur(root.left, val) || dfsRecur(root.right, val);
		}
		 
	}
	
	public static int height(TreeNode root){
		
		if (root == null) {
			return 0;
		}else{
		
			int lh = height(root.left);
			int rh = height(root.right);
			
			if (lh > rh){ 
				return lh + 1;
			}else{
				return rh + 1;
			}
		}
	
	}
	
	public static void printLayerWise(TreeNode root){
		if (root == null) return ;
		
		LinkedList<TreeNode> q = new LinkedList<TreeNode>();
		
		q.add(root);
		
		while (!q.isEmpty()){
			TreeNode node = q.poll();
			System.out.print(node.data + " ");
			
			if (node.left != null) q.add(node.left);
			if (node.right != null) q.add(node.right);
			
		}

	}
	
	public static ArrayList<LinkedList<TreeNode>> createLayerWiseLL(TreeNode root){
		if (root == null) return null;
		
		ArrayList<LinkedList <TreeNode>> res = new ArrayList<LinkedList<TreeNode>>();
		LinkedList<TreeNode> temp_holder = new LinkedList<TreeNode>();
		temp_holder.add(root);

		while (temp_holder.size() > 0){
			res.add(temp_holder);
			LinkedList<TreeNode> previousLevel = res.get(res.size() - 1);
			
			temp_holder = new LinkedList<TreeNode>();
			
			for (TreeNode previous: previousLevel){
				if (previous.left != null){
					temp_holder.add(previous.left);
				}
				if (previous.right != null){
					temp_holder.add(previous.right);
				}
			}
	
		}
		
		return res;
		
	}
	
	
	public static void inOrderRecur(BSTNode root, ArrayList<Integer> out){
		
		if (root == null) return;
		
		
		if (root.left != null){
			inOrderRecur(root.left, out);
		}
		out.add(root.data);
		
		if (root.right != null){
			inOrderRecur(root.right, out);
		}
		
		

	}
	
	
	
	
	
	public static void main(String[] args){
		
		TreeNode node = new TreeNode(5);
		node.left = new TreeNode(4);
		node.right = new TreeNode(6);
		node.left.left = new TreeNode(8);
		node.left.right = new TreeNode(0);
		node.right.left = new TreeNode(9);
		node.right.right = new TreeNode(-5);
		
		BSTNode root = new BSTNode(5);
		root.insert(root, 4);
		root.insert(root, 6);
		root.insert(root, 8);
		root.insert(root, 0);
		root.insert(root, 9);
		root.insert(root, -5);
		
		//print (bfs(node, 100));
		//print (dfsRecur(node,100));
		//printLayerWise(node);
		//print(height(node));
		
		ArrayList<LinkedList<TreeNode>> out = createLayerWiseLL(node);
		ArrayList<Integer> outArr = new ArrayList<Integer>();
		inOrderRecur(root, outArr);
		print (outArr);

	}
	
	public static void print(Object obj){
		System.out.println(String.valueOf(obj));
	}

}
