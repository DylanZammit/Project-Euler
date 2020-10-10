
public class Problem27 {
	
	static long largest;
	static long answer;
	static long temp;
	
	public static void main(String[] args) {

		
		for(int a = -999; a < 1000; a+=2){
			
			for(int b = 2; b < 1000; b++){
				
				
				if(isPrime(b)){

					temp = checkFunction(a, b);
					checkBest(a, b);
					
					temp = checkFunction(a, -b);
					checkBest(a, -b);
					
					
				}
				
			}
			
		}
		
		System.out.println(answer);

	}
	
	static void checkBest(int a, int b){
		
		if(temp > largest){
			largest = temp;
			answer = a*b;
		}
	}
	
	static boolean isPrime(int p){

		if(p%2==0){
			return false;
		}
		
		int temp = (int)Math.sqrt(p);
		
		for(int i = 3; i<=temp; i+=2){
			
			if(p%i==0){
				return false;
			}
			
		}
		
		return true;
	}
	
	static int checkFunction(int a, int b){
		
		int count = 0;
		
		int out = 0;
		
		do{

			out = count*count + a*count + b;
			
			count++;
			
		}while(out > 0 && isPrime(out));
		
		return count;
		
	}

}
