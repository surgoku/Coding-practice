package CrackingCodingInterview;

import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;



public class HeapQns {
	
	
	public static float getRunningMedian(int[] a){
		PriorityQueue<Integer> minHeap = new PriorityQueue<Integer> (100);
		PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer> (100, Collections.reverseOrder());
		
		for (int i: a){
			if (minHeap.isEmpty() &&  maxHeap.isEmpty()){
				minHeap.add(i);
			}else{
				if (minHeap.size() == maxHeap.size()){
					if (minHeap.peek() > i){
						maxHeap.add(i);
					}else{
						minHeap.add(i);
					}
				}else if (minHeap.size() > maxHeap.size()){
					if (minHeap.peek() > i){
						maxHeap.add(i);
					}else{
						maxHeap.add(minHeap.poll());
						minHeap.add(i);
					}
				}else{
					if (maxHeap.peek() < i){
						minHeap.add(i);
					}else{
						minHeap.add(maxHeap.poll());
						maxHeap.add(i);
					}
				}
			}
		}
		
		if (minHeap.size() == maxHeap.size()){
			return ((minHeap.peek() + maxHeap.peek())/(float)2);
		}else{
			if (minHeap.size() > maxHeap.size()){
				return minHeap.peek();
			}else{
				return maxHeap.peek();
			}
		}
			
	}
	
	
	public static void main(String[] args){
		
		int[] a = {5,2,7,0,13,9,15,1,24};
		
		System.out.println(getRunningMedian(a));
		
	}

}
