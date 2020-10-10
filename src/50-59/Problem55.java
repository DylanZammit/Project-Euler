import java.math.BigInteger;

public class Problem55 {

	static int answer = 0;
	
	static BigInteger b = BigInteger.ZERO;
	
	public static void main(String[] args) {

		for(int i = 1; i < 10000; i++){
			
			b = BigInteger.valueOf(i);
			
			if(isLychrel(b)){
				answer++;
			}
			
		}

		System.out.println(answer);

	}
	
	public static boolean isLychrel(BigInteger x){
		
		BigInteger rx;
		
		for(int i = 0; i < 50; i++){
			rx = reverse(x);
			x = x.add(rx);
			if(isPalindrome(x)){
				return false;
			}
			
		}
		
		return true;
		
	}
	
	public static BigInteger reverse(BigInteger x){
		
		BigInteger out = BigInteger.ZERO;
		
		while(x.compareTo(BigInteger.ZERO) == 1){
			out = out.multiply(BigInteger.TEN);
			out = out.add(x.mod(BigInteger.TEN));
			x = x.divide(BigInteger.TEN);
		}
		
		return out;
		
	}
	
	public static boolean isPalindrome(BigInteger x){
		
		String num = x.toString();
		
		int lc = 0;
		int rc = num.length()-1;
		
		while(lc < rc){
			
			if(num.charAt(lc)!=num.charAt(rc)){
				return false;
			}
			
			lc++;
			rc--;
		}
		
		return true;
	
	}

}
