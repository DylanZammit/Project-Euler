
public class Problem15 {

	//ANSWER = 40C20
	static int r = 20;
	static long answer;
	
	public static void main(String[] args) {

		int n = 2*r;
		int k = r;

		answer = getFact(n)/(getFact(k)*getFact(n-k));
		
		System.out.println(answer);

	}
	
	static long getFact(long p){
		
		long out = 1;
		
		for(int i = 1; i <= p; i++){
			
			out*=i;
			
		}
		
		return out;
		
	}

}
