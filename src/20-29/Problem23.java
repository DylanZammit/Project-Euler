import java.util.ArrayList;
import java.util.HashSet;

public class Problem23 {

	static int answer = 1;
	public static void main(String[] args) {

		ArrayList<Integer> abList = new ArrayList<Integer>();
		HashSet<Integer> abListSum = new HashSet<Integer>();
		
		
		for(int i = 2; i < 28123; i++){
			
			if(isAb(i)){
				abList.add(i);
			}
			
		}
		
		for(int i = 0; i < abList.size(); i++){
			
			for(int j = i; j < abList.size(); j++){
				
				int in = abList.get(i)+abList.get(j);

				if(!abListSum.contains(in)){
					abListSum.add(in);
				}
				
			}
			
		}
		
		for(int i = 2; i < 28123; i++){
		
			if(!abListSum.contains(i)){
				answer+=i;
			}
			
		}
		
		System.out.println(answer);

	}
	
	public static boolean isAb(int x){

		int temp = (int)Math.sqrt(x);
		
		int sum = 1;
		
		for(int i = 2; i <= temp; i++){
			
			if(x%i==0){

				sum+=i;
				
				if(x/i != i){
				
					sum+=(x/i);
				}
			}
			
		}
		
		return (sum>x)? true: false;
		
		
	}

}
