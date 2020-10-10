import java.math.BigInteger;

public class Problem26 {
	
	static int largest;
	
	static int answer;
	
	static int tries = 1000;
	
	static float currNum;

	static boolean out = false;

	static BigInteger zero = BigInteger.ZERO;
	static BigInteger ten = BigInteger.TEN;
	static BigInteger one = BigInteger.ONE;
	
	
	public static void main(String[] args) {
		
		for(int n = 3; n < 1000; n+=2){
			
			BigInteger div = new BigInteger("9");
			
			for(int b = 1; b <= tries && !out; b++){
				
				if(div.mod(BigInteger.valueOf(n)) == zero){
					out = true;
					
					if(b > largest){
						largest = b;
						answer = n;
					}
				}

				//div = ((div+1)*10)-1;
				div = ((div.add(one)).multiply(ten)).subtract(one);
				
				
			}
			
			out = false;
			
		}
		
		System.out.println(answer);

	}

}
