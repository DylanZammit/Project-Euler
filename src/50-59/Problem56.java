import java.math.BigInteger;

public class Problem56 {
	
	static int answer = 0;
	
	static int sum = 0;
	
	static BigInteger currNum;

	public static void main(String[] args) {

		for(int a = 1; a < 100; a++){
			
			for(int b = 1; b < 100; b++){
				
				currNum = BigInteger.valueOf(a).pow(b);
				
				sum = sum(currNum);
				
				if(sum> answer){
					answer = sum;
				}
				
			}
			
		}
		
		System.out.println(answer);

	}
	
	public static int sum(BigInteger x){
		
		String num = x.toString();
		
		int out = 0;
		
		for(int i = 0; i < num.length(); i++){
			
			out+=Character.getNumericValue(num.charAt(i));
			
		}
		
		return out;
		
	}

}
