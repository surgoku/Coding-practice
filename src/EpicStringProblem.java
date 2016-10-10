import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;


public class EpicStringProblem {

	
	public static String obtainSuitableStringDP(String str, HashSet<String> dict, HashMap<String, String> trackingMap){
		
		if (dict.contains(str)) return str;
		if (str==null || str.isEmpty()) return null;
		if (trackingMap.containsKey(str)) return trackingMap.get(str);
		int n = str.length();
		for (int i = 1; i< str.length(); i++){
			String left = str.substring(0, i);
			if (dict.contains(left)){
				String right = str.substring(i, n);
				String subStr = obtainSuitableStringDP(right, dict, trackingMap);
				if (subStr != null){
					return left + " " + subStr;
				}
				
			}
		}
		
		trackingMap.put(str, null);
		
		
		return str;
	}
	
	public static String obtainSuitableStringRecur(String str, HashSet<String> dict){
		
		if (dict.contains(str)) return str;
		if (str==null || str.isEmpty()) return null;
		int n = str.length();
		
		for (int i = 1; i< str.length(); i++){
			String left = str.substring(0, i);
			if (dict.contains(left)){
				String right = obtainSuitableStringRecur(str.substring(i,n), dict);
				if (right != null){
					return left + " " + right;
				}
			}
		}
		
		
		return null;
	}
	
	
	public static void main(String[] args){
	
		String str = "mynameischandra";
		HashSet<String> dict = new HashSet<String>();
		dict.add("my");
		dict.add("name");
		dict.add("is");
		dict.add("chandra");
		dict.add("nam");
		dict.add("and");
		HashMap<String, String> trackingMap = new HashMap<String, String>();
		print(obtainSuitableStringRecur(str, dict));
		print (obtainSuitableStringDP(str,  dict,  trackingMap));
		
	}
	
	public static void print(Object str){
		System.out.println(str);
	}
}
