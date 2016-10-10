package hackerRank;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class StandardInput {

	public static void main (String[] args){
		
			
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		
        Scanner scan = new Scanner(System.in);
        /* Declare second integer, double, and String variables. */
        int secondInt = 0;
        double secondDouble = 0.0;
        String secondStr = "";
        /*
        if (scan.hasNextInt()){
            secondInt = scan.nextInt();
        } 
        
        if (scan.hasNextDouble()){
            secondDouble = scan.nextDouble();
        } 
        
        
        secondStr = scan.nextLine();

        System.out.println(i+secondInt);
        System.out.println(d+secondDouble);
        System.out.println(s+"yoyo");
        */
        
        
         
         String [] grid = {"---", "-m-", "--p"};
         //displayPathtoPrincess(3, grid);
         //printStairs();
         
         
         
         //String s1 = String.valueOf(arr.length);
         int[] arr2 = {1,2,3,4,10,20,30,40,100,200};
         solve(arr2,10,4);
         
        
	}
	
	static void displayPathtoPrincess(int n, String [] grid){
	    int bot_x = 0;
	    int bot_y = 0;
	    int p_x = 0;
	    int p_y = 0;
	    
	    char[][] newGrid = new char[n][n];
	    
	    for (int i=0; i < n; i++){
	    	char[] temp = grid[i].toCharArray();
	    		newGrid[i] = temp;    	
	    }
	    
	    
	    
	    for (int i = 0 ; i < n; i++){
	    	for (int j =0; j < n; j++){
		        if (newGrid[i][j] == 'm'){
		            bot_y = i;
		            bot_x = j;
		        }
		        if (newGrid[i][j]== 'p'){
		            p_y = i;
		            p_x = j;
		        } 
	    	}
	    }
	    
	    print(bot_y +" "+ bot_x);
	    print(p_y +" "+ p_x);
	    
	    int net_x = bot_x-p_x;
	    int net_y = bot_y - p_y;
	    
	    if (net_x < 0){
	    	while(net_x !=0){
	    		print("RIGHT");
	    		net_x += 1;
	    	}
	    		
	    }else if (net_x > 0){
	    	while(net_x !=0){
	    		print("LEFT");
	    		net_x -= 1;
	    	}
	    }
	    
	    if (net_y < 0){
	    	while(net_y !=0){
	    		print("Down");
	    		net_y += 1;
	    	}
	    		
	    }else if (net_y > 0){
	    	while(net_y !=0){
	    		print("Up");
	    		net_y -= 1;
	    	}
	    }
	    
	    
	    
	  }
	
	public static void print (Object str){
		System.out.println(String.valueOf(str));
	}
	
	public static void printStairs(){
		int n = 6;
        ArrayList<String> str = new ArrayList<>(n);
        char[] s = new char[n];
        for (int i=0; i<n; i++){
            s[i] = '#';
            str.add("");
        }

        for (int i =0; i< n; i++){
            str.set(n-i-1, String.valueOf(s));
            s[i] = ' ';
            
            
        }
        
        for (String s_i: str){
            print(s_i);
        }
	}
	
	public static boolean checkTaken(HashSet<String> set, int i, int j){
        String out_one = String.valueOf(i) + "," + String.valueOf(j);
        String out_two = String.valueOf(j) + "," + String.valueOf(i);
        
        if (set.contains(out_one) || set.contains(out_two)){
            return true;
        }
        
        return false;
    }
   
    public static void solve(int[] arr, int N, int K) {
    	int[] sortedArr = arr;
        Arrays.sort(sortedArr);
        long unfairness = 0;
        long unfairnessSecond = 0;
         
        int startCoeff = K*-1 + 1;
        for (int i =0; i < K; i++){
        	unfairness += (startCoeff*sortedArr[i]);
        	startCoeff+=2;
        }
        
         
         
        int[] diffArr = new int[N];
        diffArr[0] = sortedArr[0];
        long out = 0;
        startCoeff = K*-1 + 1;
        for (int i =1; i < N; i++){
            diffArr[i] = diffArr[i-1] + sortedArr[i];
        }
        
        for (int i = 0, j=i+K-1; j<N; j++,i++ ){
            if (i >0){
                unfairnessSecond += sortedArr[i-1]*(K-1) + sortedArr[j]*(K-1);
                unfairnessSecond -= diffArr[j-1]*2 - diffArr[i-1]*2;
                out = Math.min(unfairnessSecond, out);
            }else{
                for(int p =i; p<=j;p++ ){
                    
                    unfairnessSecond += sortedArr[p]*startCoeff;
                    startCoeff +=2;
                }
                out = unfairnessSecond;
            }
        }
        
         System.out.println(out);
         
         /*
        HashSet<String> set = new HashSet<String>();
        for (int i = 0; i <K; i++){
            for (int j = 0; j <K; j++){
                if (i !=j && !checkTaken(set,i, j)){
                    unfairness += Math.abs(sortedArr[i] - sortedArr[j]);
                } 
                String temp = String.valueOf(i) + ',' +  String.valueOf(j);
                set.add(temp); 
           }
        }
        */
        //System.out.println(unfairness);
   
    }
    
    public static class PairInstance implements Comparable<PairInstance>{
    	int first;
    	int second;
    	int diff;
    	
    	public PairInstance(int i, int j){
    		this.first = i;
    		this.second = j;
    		this.diff = Math.abs(i-j);
    	}
    	
    	public int compareTo(PairInstance pair){
    		return Double.compare(this.diff, pair.diff);
    	}
    	
    }
	
}
