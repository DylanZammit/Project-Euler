
import java.math.BigInteger;

public class Problem48 {
	
	static BigInteger answer = BigInteger.ZERO;

	public static void main(String[] args) {

		
		for(int i = 1; i <= 1000; i++){
			

			BigInteger j = BigInteger.valueOf(i);
			
			answer = answer.add(j.pow(i));
		}
		
		System.out.print(answer);

	}

}
