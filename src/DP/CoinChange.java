package DP;

import java.util.ArrayList;

public class CoinChange {
	
	
	public static int printCountsRecur(int[] arr, int m, int N){

		if (N==0){ return 1;}
		if (N < 0){return 0;}		
		if (m<=0 && N >=1){return 0;}
		
		return printCountsRecur(arr, m-1,N) + printCountsRecur(arr, m, N-arr[m-1]);

	}
	
	public static long printCountsDP(int[] arr, int m, int N){

		if (N==0){ return 1;}
		if (N < 0){return 0;}		
		if (m<=0 && N >=1){return 0;}
		
		// building table for coins-N table: to address the sub-problems
		long[][] dpArray = new long[N+1][m];
		
		//instantiating the first column the base case of 0
		for (int i =0; i < m; i++){
			dpArray[0][i] =1;
		}
		
		for (int i =1; i<N+1; i++){
			for (int j=0; j < m; j++){
				long smalerrSubSum =0;
				long directSum = 0;
				if (i-arr[j] >= 0){
					directSum = dpArray[i-arr[j]][j];
				}
				if (j>=1){
					smalerrSubSum = dpArray[i][j-1];
				}	
				dpArray[i][j] = directSum + smalerrSubSum;
			}
		}
		
		return dpArray[N][m-1];

	}
	
	public static void main(String[] args ){
		int[] arr = {1,2,3};
		int n = 250;
		
		int[] arr2 = {8 ,47 ,13 ,24 ,25 ,31 ,32 ,35 ,3 ,19 ,40 ,48 ,1 ,4 ,17 ,38 ,22 ,30 ,33 ,15 ,44 ,46 ,36 ,9 ,20,49};
		
		//print(printCountsRecur(arr,arr.length, n));
		print(printCountsDP(arr2,arr2.length, n));
	}
	
	public static void print(Object str){
		System.out.println(String.valueOf(str));
	}

}
