
public class Problem216 extends Functions{

	static int answer = 0;
	
	final static int cap = 10000;
	
	public static void main(String[] args) {

		for(int n = 2; n <= cap; n++){
			if(isPrime(2*n*n-1)){
				answer++;
				//System.out.println(n);
			}
		}

		System.out.println(answer);

	}

}
