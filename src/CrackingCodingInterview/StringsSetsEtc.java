package CrackingCodingInterview;

public class StringsSetsEtc {
	
	public static void permutationsOfStringRecur(String str, String prefix){
		
		if (str.length() == 0){
			print(prefix);
		}else{
			for (int i=0; i< str.length(); i++){
				String temp = str.substring(0,i) + str.substring(i+1);
				permutationsOfStringRecur(temp, prefix + str.charAt(i));
			}			
		}
		
	}
	
	public static long  O(int n)
	{
	    if (n == 0)
	        return 1;
	    else 
	       return 2+ n * O(n-1);
	}

	
	
	public static void main(String[] args){
		
		String str = "abc";
		permutationsOfStringRecur(str, "");
		print("order of complexity: ");
		print(O(5));
		
	}
	
	public static void print(Object obj){
		System.out.println(String.valueOf(obj));
	}
	

}
