
public class Problem58 {
	
	static int totalDiags = 1;
	
	static int totalPrimes = 0;
	
	static float ratio = 1;
	
	static int side = 1;
	
	static int number = 1;

	public static void main(String[] args) {

		while(ratio > 0.1f){
			
			int count = 0;
			
			while(count < 4){
				
				number+=side+1;
				
				if(isPrime(number) && count != 3){
					totalPrimes++;
				}
				
				count++;
				
			}
			totalDiags+=4;
			side+=2;
			ratio = (float)totalPrimes/totalDiags;
		}
		
		System.out.println(side);
		

	}
	
	public static boolean isPrime(int x){
		
		if(x%2==0){
			return false;
		}
		
		int temp = (int)Math.sqrt(x);
		
		
		for(int i = 3; i <= temp; i+=2){
			
			if(x%i==0){
				return false;
			}
			
		}
		
		return true;
		
	}

}
