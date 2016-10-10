package DP;

import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;



public class DP {
	
	public static int maxSubContiguousArray(int[] arr){
		int currMaxSum = arr[0];
		int tempSum = arr[0];
		boolean allNegative = true;
		if (tempSum <0){
			tempSum = 0;
		}
		if (currMaxSum <0){
			currMaxSum =0;
		}
		for (int i = 1; i < arr.length; i++){
			tempSum += arr[i];
			if (tempSum >= currMaxSum){
				currMaxSum = tempSum;
			}
			if (tempSum <0){
				tempSum = 0;
			}
			
			if (arr[i] > 0){
				allNegative = false;
			}
			
			
		}
		
		if (allNegative){
			Arrays.sort(arr);
			return arr[arr.length-1];
		}else{
			return currMaxSum;
		}
		
	}
	
	public static int maxSubNonContiguousArray(int[] arr){
		int currMaxSum = arr[0];
		int tempSum = arr[0];
		if (tempSum <0){
			tempSum = 0;
		}
		boolean allNegative = true;
		if (currMaxSum <0){
			currMaxSum =0;
		}
		for (int i = 1; i < arr.length; i++){
			if (arr[i] > 0){
				currMaxSum += arr[i];
				allNegative = false;
			}
		}
		
		if (allNegative){
			Arrays.sort(arr);
			return arr[arr.length-1];
		}else{
			return currMaxSum;
		}
	}
	
	public static int longestIncreasingSubsequence(int[] a){
		int n = a.length;
		int[] out = new int[n];
		for (int i=0; i < n; i++){
			out[i] = 1;
		}
		
		for (int i = 1; i < n; i++){
			for (int j = 0; j < i; j++){
				if (a[i]> a[j] && out[i]< out[j] + 1){
					out[i] = out[j] + 1;
					print( out[i]);
					
				}
			}
		}
		
		int max = 0;
		
		for (int i: out){
			if (out[i] > max){
				max = out[i];
			}
		}
		
		return max;
		
	}
	
	
	public static void main(String[] args){
		
		int[] arr = {1 ,2, 3, 4};
		int[] arr2 = {2, -1, 2, 3, 4, -5};
		int[] arr3 = {2, -1, 2, 3, 4, -5};
		
		/*
		Scanner in = new Scanner(System.in);
		boolean testCaseCheck = false;
		ArrayList<int[]> providedLists = new ArrayList<int[]>();
		if (in.hasNextInt()){
			int T = in.nextInt();
			if (T >0 && T < 11){
				for (int i=0; i < T; i++){
					if (in.hasNextInt()){
						int arrLength = in.nextInt();
						if (arrLength >0 && arrLength < 100001){
							int[] arrLocal = new int[arrLength];
							boolean localTestFail = false;
							for (int j =0; j< arrLength; j++){
								if (in.hasNextInt()){
									arrLocal[j] = in.nextInt();
									if (arrLocal[j] < -10000 || arrLocal[j] > 10000){ 
										localTestFail = true;
									}
									
								}else{
									localTestFail = true;
								}
							}
							if (!localTestFail){
								providedLists.add(arrLocal);
								
							}
						}
					}
				}
			}
		}
		*/
		
		/*
		for(int[] arrLocal : providedLists){
			int firstOut = maxSubContiguousArray(arrLocal);
			int secondOut = maxSubNonContiguousArray(arrLocal);
			print(firstOut + " " + secondOut);
		}
		*/
		print(longestIncreasingSubsequence(arr2));
		
		
		//print(maxSubContiguousArray(arr));
		//print(maxSubNonContiguousArray(arr2));
		
	}
	
	public static void print(Object str){
		System.out.println(String.valueOf(str));
	}

}
