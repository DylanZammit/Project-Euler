
import java.math.BigInteger;

public class Problem20 {

	static BigInteger fact = BigInteger.ONE;
	
	static long answer = 0;
	
	public static void main(String[] args) {

		for(int i = 1; i <= 100; i++){
			fact = fact.multiply(BigInteger.valueOf(i));
		}
		
		String num = fact.toString();
		
		for(int i = 0; i < num.length(); i++){
			
			answer+=Character.getNumericValue(num.charAt(i));
			
		}
		
		System.out.println(answer);
		
	}

}
