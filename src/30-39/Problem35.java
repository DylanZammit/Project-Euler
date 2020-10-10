
public class Problem35 {
	
	static int answer = 1;

	public static void main(String[] args) {

		for(int i = 3; i < 1000000; i++){
			
			if(isCircPrime(i)){
				answer++;
			}
			
		}
		System.out.println(answer);

	}
	
	public static boolean isPrime(int x){
		
		int max = (int)Math.sqrt(x);
		
		for(int k = 2; k <= max; k++){
			
			if(x%k==0){
				return false;
			}
			
		}
		
		return true;
	}
	
	public static boolean isCircPrime(int x){
		
		int numLength = (int)(Math.log10(x)+1);
		
		int lastDig;
		
		for(int i = 0; i < numLength; i++){
			
			if(!isPrime(x)){
				return false;
			}
			lastDig = x%10;
			x/=10;
			x+=(lastDig*Math.pow(10, numLength-1));
			
			
		}
		
		return true;
	}

}
