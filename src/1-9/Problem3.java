
public class Problem3 {

	static long answer=0;
	
	public static void main(String[] args) {

		primeFactors(600851475143L);
		System.out.println(answer);
	}
	
	static void primeFactors(long i){
		long loFac;
		
		if(!isPrime(i)){
			loFac = getLowestFactor(i);

			primeFactors(loFac);
			primeFactors(i/loFac);
			
		}else{
			if(i>answer){
				answer = i;
			}
		}
		
		
	}
	
	static long getLowestFactor(long i){
		
		for(long count = 2; count < i; count++){
			if(i%count==0){
				return count;
			}
		}
		return 0;
		
	}
	
	static boolean isPrime(long i){
		if(i==2){
			return true;
		}
		
		if(i%2 == 0){
			return false;
		}
		
		for(long count = 3; count < (i/2)+1; count+=2){
			if(i%count == 0){
				return false;
			}
		}
		
		return true;
	}
	

}
