package hackerRank;
import java.math.BigInteger;
import java.util.Scanner;


public class Fib {

	
	public static int fibRec(int n){
		if (n==0){
			return 0;
		}
		else if (n==1){
			return 1;
		}else{
			return (fibRec(n-1) + fibRec(n-2));
		}
		
		
	
	}
	
	public static long fibDP(int n){
		long[] outArr = new long[n+1];
		outArr[0] = 0;
		outArr[1] = 1;
		for (int i=2; i<= n; i++){
			outArr[i] = outArr[i-1] + outArr[i-2];
		}
		
		return outArr[n];
		
	}
	
	public static BigInteger fibRevisedDP(int a, int b, int n){
		long[] outArr = new long[n+1];
		BigInteger[] series = new BigInteger[n];

		outArr[0] = a;
		outArr[1] = b;
		series[0] = BigInteger.valueOf(a);
		series[1] = BigInteger.valueOf(b);
		for (int i=2; i< n; i++){
			outArr[i] = (long) (Math.pow(outArr[i-1],2) + outArr[i-2]);
			series[i] = series[i-2].add(series[i-1].multiply(series[i-1]));
		}
		
		return series[n-1];
		
	}
	
	public static void main(String[] args){
		

		//print(fibRec(50));
		Scanner in = new Scanner(System.in);
        int A,B,N;
        String a = in.next();
        String b = in.next();
        String n = in.next();
        A = Integer.parseInt(a);
        B = Integer.parseInt(b);
        N = Integer.parseInt(n);
		print(fibRevisedDP(A, B, N));
		
		
		
	}
	
	public static void print(Object str){
		System.out.println(String.valueOf(str));
	}
}
