package GlassDoor;

import java.util.ArrayList;
import java.util.BitSet;
import java.util.HashSet;


public class Google {

	public static String toBinary(int num) {
	    StringBuffer sb = new StringBuffer();

	    for (int i = 0; i < 32; i++) {
	      sb.append(((num & 1) == 1) ? '1' : '0');
	      num >>= 1;
	    }

	    return sb.reverse().toString();
	  }
	
	public static HashSet<String> stringPermsSpecialStr(String str){
		//Given a string with 0, 1 and "?" character. "?" can be 0 or 1, find all perms of string
		// Locate all "?". Say total "?" = n
		// find all permutations of a string of size n with 0 and 1, using bit: all numbers in bit
		// with less than 2^n size. get their bit form of the string. each will be unique.
		// once found all perms of size n string of total of 2^n perms, insert that perm at "?" locations
		// in original string
		
		if (str == null) return null;
		HashSet<String> out = new HashSet<String>();
		
		ArrayList<Integer> holder = new ArrayList<Integer>();
		
		for (int i = 0; i < str.length(); i++){
			if (str.charAt(i)  == '?') {
				holder.add(i);
			}
		}
		
		int n = holder.size();
		
		
		ArrayList<String> perms = new ArrayList<String>();
		
		for (int i = 0; i < Math.pow(2,n); i++){
			String s = Integer.toBinaryString(i);
			perms.add(s);
			//print (s.length());
			if (s.length() < n){
				while (! (s.length() == n)){
					s = "0" + s;
				}
			}
		}
		
		
		for (String s: perms){
			StringBuilder outStr = new StringBuilder(str);
			
			for (int i=0; i < s.length(); i++){
				print (holder.get(i));
				print(s);
				outStr.setCharAt(holder.get(i), s.charAt(i));
			}
			
			
			out.add(outStr.toString());
		}
		
		for (String s: out){
			print(s);
		}
		
		
		
		
		return out;
	}
	
	
	public static void main(String[] args){
		
		String s = "1?0?1?0";
		stringPermsSpecialStr(s);
		
		
	}
	
	public static void print(Object obj){
		System.out.println(String.valueOf(obj));
	}
}
