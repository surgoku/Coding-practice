package JavaBasics;

import java.util.ArrayList;
import java.util.HashSet;

public class TwoSumImpl implements ImplEx {
	
	ArrayList<Integer> store = new ArrayList<Integer>();
	HashSet<Integer> sums = new HashSet<Integer>();
	
	
	public void Store(int input){
		if (! store.contains(input)){
			store.add(input);
		}
	}
	
	public Boolean Test(int input){
		for (int in: store){
			int sum = in+input;
			if (sums.contains(sum)){
				return true;
			}
			sums.add(sum);
		}
		return false;
	}

}
