import java.util.ArrayList;

public class Problem50 {

	static int answer = 0;
	
	static int sum = 0;
	
	static int consCount = 0;
	
	static int topCount = 0;
	
	static boolean found = false;
	
	static ArrayList<Integer> prime = new ArrayList<>();
	
	public static void main(String[] args) {
		
		for(int i = 2; !found; i++){
			
			if(isPrime(i)){
				
				if(sum+i<1000000){
					prime.add(i);
					sum+=i;
					consCount++;
				}else{
					found = true;
				}
				
			}
			
		}
		
		int temp = sum;
		
		int tempCount;
		
		int begPct = 0;
		
		boolean redundant;
		
		for(int i = 0; i < prime.size(); i++){
			
			tempCount = consCount-i;
			
			temp-=begPct;
			
			if(isPrime(temp) && tempCount > topCount){
				
				topCount = tempCount;
				answer = temp;
				
			}
			
			redundant = false;
			
			for(int j = prime.size()-1; j > 0 && !redundant; j--){
				
				temp-=prime.get(j);

				tempCount--;
				
				if(isPrime(temp) && tempCount > topCount){
					
					topCount = tempCount;
					answer = temp;
					
				}
				
				if(tempCount < topCount){
					
					redundant = true;
					
				}

			}
			temp = sum;
			begPct+=prime.get(i);
			
		}
		
		System.out.println(answer + " " +topCount);
		
	}
	
	public static boolean isPrime(int x){
		
		if(x == 2){
			return true;
		}
		
		int max = (int)Math.sqrt(x);
		
		for(int i = 2; i <= max; i++){
			if(x%i==0){
				return false;
			}
		}
		
		return true;
		
	}

}
