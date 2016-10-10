package CrackingCodingInterview;

import java.util.ArrayList;
import java.util.Arrays;

public class ArraysChapter1 {
	
	public static boolean uniqueCharacterCheck(String str){
		
		if (str.length() >256){
			return false;
		}
		
		boolean charSet[] = new boolean[256];
		
		for (int i=0; i < str.length(); i++){
			int charInt = str.charAt(i);
			if (!charSet[charInt]){
				charSet[charInt] = true;
			}else{
				return false;
			}	
		}
		return true;
	}
	
	public static boolean uniqueCharacterCheckUsingBit(String str){
		if (str.length() >256){
			return false;
		}
		int bit =0;
		boolean charSet[] = new boolean[256];
		for (int i=0; i < str.length(); i++){
			int charInt = str.charAt(i);
			if ((bit & (1 << charInt)) == 0)	{
				bit |= (1 <<charInt);
			}else{
				return false;
			}
		}
		return true;
	}
	
	public static int[][] rotateMatrix(int[][] matrix, int n){
		
		// outer layers: need to do till n/2 since there are n/2 layers.
		for (int layer = 0; layer < n/2 ; ++layer){
			
			int start = layer;
			int end = n-1 -layer;
			
			for (int i = start; i < end; ++i){
				int offset = i-start;
				int topStart = matrix[start][i];
				int left = matrix[end-offset][start];
				matrix[start][i] = left;
				int below = matrix[end][end - offset];
				matrix[end-offset][start] = below;
				int right = matrix[i][end];
				matrix[end][end-offset] = right;
				matrix[i][end] = topStart;
			}
			
		}
		
		
		return matrix;
	}
	
	
	
	public static boolean isPermutation(String s, String t){
		
		if (s.length() != t.length()) return false;
		
		s = s.toLowerCase();
		t = t.toLowerCase();
		
		int[] charCount = new int[128];
		
		for (char c: s.toCharArray()){
			int val = c - 'a';
			charCount[val]++;
		}
		
		for (char c: t.toCharArray()){
			int val = c - 'a';
			charCount[val]--;
			
			if (charCount[val] < 0){
				return false;
			}
		}
		
		
		return true;
		
	}
	
	public static String compressString(String in){

		
		StringBuilder sb = new StringBuilder();
		
		int count = 1;
		char lastChar = in.charAt(0);
		
		for (int i = 1; i < in.length(); i++){
			if (in.charAt(i) == in.charAt(i-1)){
				count++;
			}else{
				sb.append(lastChar);
				sb.append(String.valueOf(count));
				count = 1;
				lastChar = in.charAt(i);
			}
		}
		
		sb.append(lastChar);
		sb.append(count);
		
		
			
		String out =  sb.toString();
		return (out);
	}
	
	
	public static void main(String[] args){
		
		//print(uniqueCharacterCheckUsingBit("YHS$!@%K"));
		int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
		int n = matrix.length;
		matrix = rotateMatrix(matrix, n);
		
		for (int i =0; i < n; i++ ){
			print(Arrays.toString(matrix[i]));
		}
		
		String in = "abbccccccdaaeghhhkllg";
		print(compressString(in));
		print(isPermutation("GOD", "god"));
		
		
				
	}
	
	public static void print(Object str){
		System.out.println(String.valueOf(str));
	}
	
}
