package DP;

public class Candies {

	public static int requiredCandies(int[] ratingArr){
		
		int[] candies = new int[ratingArr.length];
		int N = ratingArr.length;
		if (N <=1){
			return N;
		}
		candies[0] =1;
		for (int i=1; i < N; i++ ){
			if (ratingArr[i] > ratingArr[i-1]){
				candies[i] = candies[i-1] +1;
			}else{
				candies[i] =1;
			}
		}
		for (int i=N-1; i >0; i--){
			if (ratingArr[i-1]>ratingArr[i]){
				candies[i-1] = Math.max(candies[i]+1, candies[i-1]);
			}
		}
		
		int res=0;
		for (int i=0; i< N; i++){
			res += candies[i];
		}
		return res;	
	}
	
	public static void main(String[] args ){
		int[] arr = {1,2,3};
		int n = 250;
		
		//int[] ratingArr = {8 ,47 ,13 ,24 ,25 ,31 ,32 ,35 ,3 ,19 ,40 ,48 ,1 ,4 ,17 ,38 ,22 ,30 ,33 ,15 ,44 ,46 ,36 ,9 ,20,49};
		
		int[] ratingArr = {1,2,2};
		print(requiredCandies(ratingArr));
		
	}
	
	public static void print(Object str){
		System.out.println(String.valueOf(str));
	}
}
