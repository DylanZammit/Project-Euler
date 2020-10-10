
public class Problem10 {
	
	static long answer = 2;
	
	public static void main(String[] args) {
		
		for(long p = 3; p<2000000; p+=2){
			
			if(checkPrimality(p)){
				answer+=p;
			}
		}
		
		System.out.println(answer);
		
	}
	
	static boolean checkPrimality(long p){
		
		long temp = (long)Math.sqrt(p);
		
		for(long i = 3; i <= temp; i+=2){
			if(p%i==0){
				return false;
			}
		}
		return true;
		
	}
}
