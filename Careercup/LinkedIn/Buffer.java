package LinkedIn;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Buffer {

	public static ArrayList<Integer> findFactors(int n){
		HashSet<Integer> resSet = new HashSet<Integer>();
		
		
		for (int i = 2; i <= n/2; i++){
			if (n % i == 0){
				resSet.add(i);
				resSet.add(n/i);
				//n = n/i;
			}
		}
		resSet.add(1);
		resSet.add(n);
		
		ArrayList<Integer> res = new ArrayList<Integer>(resSet);
		return res;
	}
	
	
	public static int coinChangeRecur(int n, int[] coins, int i){
		//time complexity 2^m
		if (n < 0) return 0;
		if (n == 0) return 1;
		
		if (i == coins.length && n >0){
			return 0;
		}
		
		return (coinChangeRecur(n-coins[i], coins, i) + coinChangeRecur(n, coins, i+1));
	}
	
	public static int coinChangeDP(int n, int[] coins){
		//http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/
		int[][] matrix = new int[coins.length+1][n+1];
		
		
		// when amount is 0, there one case with each coin
		for (int i=0 ; i <= coins.length; i++){
			matrix[i][0] = 1;
		}
		
		//amount > 0, but no coins given
		for (int j=1; j <= n; j++){
			matrix[0][j] = 0;
		}
		
		
		for (int i=1; i <= coins.length; i++){
			for (int j = 1; j<= n; j++){
				// check if coin value less than amount left
				if (coins[i-1] <= j){
					matrix[i][j] = matrix[i-1][j] + matrix[i][j-coins[i-1]];
				}else{
					// coin val exceeded the required sum
					matrix[i][j] = matrix[i-1][j];
				}
			}
		}
		
		
		return (matrix[coins.length][n]);
		
	}
	
	public static void minimumCoinProblemDP(){
		
	}
	
	
	public static void main(String[] args){
		ArrayList<Integer> out = findFactors(8);
		//out = out.sort();
		//Collections.sort(out);
		//print(out);
		int n = 100;
		int[] coins = {1,2,3,5,10};
		print(coinChangeRecur(n, coins, 0));
		print (coinChangeDP(n, coins));
		
		
	}
	
	public static void print(Object obj){
		System.out.println(String.valueOf(obj));
	}
}
