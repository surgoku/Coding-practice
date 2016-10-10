package Buffer;

import java.util.ArrayList;
import java.util.HashSet;

public class Buffer {

	public static ArrayList<Integer> primeFactors(int n){
		
		HashSet<Integer> set = new HashSet<Integer>();
		ArrayList<Integer> out = new ArrayList<Integer>();
		
		for (int i=2; i<= n/2; i++){
			if (n%i == 0 && !set.contains(i)){
				out.add(i);
				int quotient = n/(2*i);
				for (int j=1 ; j<= quotient; j++ ){
					set.add(j*i);
				}
			}
		}
		
		return out;
	}
	
	
	public static double findSqrt(double n){
		double ans = 0.0;
		double start = 0.0;
		double end = n;
		
		double thresh = 0.0005;
		
		while (start < end){
			ans = (end+start)/2;
			
			if (Math.abs(ans*ans -n) < thresh){
				return ans;
			}
			
			if (ans*ans < n){
				start = ans;
			}else{
				end = ans;
			}
			
			
		}
		
		return ans;

	}
	
	public static void main(String[] args){
		//print(primeFactors(100));
		print(findSqrt(25));
	}
	
	public static void print (Object obj){
		System.out.println(String.valueOf(obj));
	}
}
