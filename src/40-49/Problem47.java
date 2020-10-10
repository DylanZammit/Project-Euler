import java.util.HashSet;

public class Problem47 {

	static boolean found = false;

	static HashSet<Integer> hs = new HashSet<Integer>();
	
	final static int n = 4;
	
	static int answer;
	
	public static void main(String[] args) {

		int i = 2;
		int ansCount = 0;
		
		while(!found){
			
			getPrimeFactors(i);
			
			if(hs.size() == n){
				
				if(ansCount == 0){
					answer = i;
				}
				
				ansCount++;
				
			}else{
				
				ansCount = 0;
				
			}
			
			if(ansCount == n){
				
				found = true;
				
			}
			
			hs.clear();
			
			i++;
		}
		
		System.out.println(answer);

	}
	
	public static void getPrimeFactors(int i){
		
		if(isPrime(i)){
			
			if(!hs.contains(i)){
				hs.add(i);
			}
			
			
		}else{
			
			int fact = getLoFac(i);
			
			getPrimeFactors(fact);
			getPrimeFactors(i/fact);
			
		}
		
		
	}
	
	public static int getLoFac(int x){

		int temp = (int)Math.sqrt(x);
		
		for(int i = 2; i <= temp; i++){
			
			if(x%i==0){
				return i;
			}
			
		}
		
		return -1;
		
	}
	
	public static boolean isPrime(int x){
		
		int temp = (int)Math.sqrt(x);
		
		
		for(int i = 2; i <= temp; i++){
			
			if(x%i==0){
				return false;
			}
			
		}
		
		return true;
		
	}

	
	
}
