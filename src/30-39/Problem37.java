
public class Problem37 {
	
	static int answer = 0;
	
	static int count = 0;
	
	public static void main(String[] args) {
		
		for(int i = 10; count < 11; i++){
			
			if(isPrime(i)){
				
				if(leftAlg(i) && rightAlg(i)){
					System.out.println(i);
					answer+=i;
					count++;
				}
				
			}
			
		}
		
		System.out.println(answer);
		
	}
	
	public static boolean leftAlg(int x){
		
	    while (x > 0) {
	    	if(!isPrime(x)){
				return false;
			}
	        x%=(int) Math.pow(10, (int) Math.log10(x));
	    }
		return true;
	}
	
	public static boolean rightAlg(int x){
		while(x>0){
			if(!isPrime(x)){
				return false;
			}
			x/=10;
		}
		return true;
	}
	
	
	public static boolean isPrime(int x){
		
		if(x == 1){
			return false;
		}else if(x == 2){
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
