import java.math.BigInteger;

public class Problem97 {
	
	public static void main(String[] args) {

		BigInteger out = BigInteger.valueOf(28433).multiply(BigInteger.valueOf(2).pow(7830457)).add(BigInteger.ONE).mod(BigInteger.valueOf(10000000000L));

		System.out.println(out);
		
	}

}
