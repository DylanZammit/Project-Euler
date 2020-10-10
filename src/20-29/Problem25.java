import java.math.BigInteger;

public class Problem25 {
	
	static BigInteger fibNum = BigInteger.ZERO;

	static BigInteger one = BigInteger.ONE;
	
	static long index = 3;
	
	public static void main(String[] args) {

		fib(one, one);

	}
	
	static void fib(BigInteger a, BigInteger b){
		
		fibNum = a.add(b);
		
		if(fibNum.toString().length()==1000){
			
			System.out.println(index);
			
		}else{
			index++;
			fib(b, fibNum);
		}
		
	}
	

}
