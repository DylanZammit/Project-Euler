
public class Problem206 {

	static long max = (long) Math.sqrt(1929394959697989900L);
	
	static long min = (long) Math.sqrt(1020304050607080900L);

	public static void main(String[] args) {

		min = (min/10)*10;

		for(long i = min; i < max; i+=10){
			if(inForm(i*i)){
				
				System.out.println(i);
				
			}
		}

	}
	
	static boolean inForm(long l){
		
		long temp = l/100;
		
		int div = 10;
		for(int j = 9; j >= 1; j--){
			
			if(temp%div != j){
				
				return false;
				
			}
			
			temp/=100;
			
		}
		
		return true;
		
	}

}
