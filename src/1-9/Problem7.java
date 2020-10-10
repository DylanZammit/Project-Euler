
public class Problem7 {
	
			
	public static void main(String[] args) {

		long n = 3;
		int count = 1;
		
		while(count<10001){

			if(isPrime(n)){
				count++;
			}
			n+=2;
		}
		System.out.println(n-2 + " : " + count);
		

	}
	
	static boolean isPrime(long n){
		
		int temp = (int)(Math.sqrt(n));
		
		for(int i = 3; i<=temp; i+=2){
			if(n%i==0){
				return false;
			}
		}
		
		return true;
	}

}
