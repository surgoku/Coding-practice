package Buffer;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Sorting {
	
	public static List<Integer> mergeSort(List<Integer> input){
		List<Integer> result = new ArrayList<Integer>();
		if (input.size() <2){
			return input;
		}
		int n = input.size();
		List<Integer> left = mergeSort((List<Integer>) input.subList(0,n/2));
		List<Integer> right = mergeSort((List<Integer>) input.subList(n/2,n));
		
		int i = 0;
		int j = 0;
		
		List<Integer> toRemoveLeft = new LinkedList<Integer>();
		List<Integer> toRemoveRight = new LinkedList<Integer>();
		
		while(left.size() > i   && right.size() > j){
			
			//if (left.size() > 0 && right.size() > 0){
			
				if (left.get(i) > right.get(j)){
					result.add(right.get(j));
					j++;
				}else{
					result.add(left.get(i));
					i++;
				}
			//}
		}
		

		for (int in: left.subList(i,left.size())){
			result.add(in);
		}
		for (int in: right.subList(j,right.size())){
			result.add(in);
		}
			
		return result;
	}
	
	public static void main(String[] args){
		
		ArrayList<Integer> arr = new ArrayList<Integer>();
		arr.add(0);
		arr.add(5);
		arr.add(-109);
		arr.add(10);
		arr.add(2);
		arr.add(100);
		arr.add(2);
		arr.add(5);
		arr.add(3);
		
		print(arr);
		print(mergeSort(arr));
		
		
	}
	
	public static void print(Object obj){
		System.out.println(String.valueOf(obj));
	}

}
