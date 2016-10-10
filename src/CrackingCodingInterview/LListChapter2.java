package CrackingCodingInterview;

import java.util.BitSet;
import java.util.HashSet;



public class LListChapter2 {
 // All the questions in the default package of DS
	
	public static void removeDuplicatesLL(LLNode in){
		if (in == null) return;
		BitSet b = new BitSet();
		
		HashSet<Integer> set = new HashSet<Integer>();		
		
		while (in != null){
			int val = in.val;
			if (b.get(val)){
				in.val = in.next.val;
				in.next = in.next.next;
			}else{
				b.set(val);
				set.add(val);
				in = in.next;	
			}
		}
	}
	
	public static void printKToLast(LLNode in, int k){	
		if (k< 0 || in == null) return;
		int counter = 0;
		while (in != null){
			if (counter == k) {
				print (in.val);
			}else {
				counter ++;
			}
			in = in.next;
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
		
		//removeDuplicatesLL(root);
		printKToLast(root, 2);
		
		/*
		LLNode temp = root;
		while(temp != null){
			print(temp.val);
			temp = temp.next;
		}
		*/
		
		
	}
	
	public static void print(Object obj){
		System.out.println(String.valueOf(obj));
	}
}
