
public class Problem34 {
	
	static long answer = 0;

	public static void main(String[] args) {
		
		for(int i = 3; true; i++){
			
			if(i == sumFactDigits(i)){
				answer+=i;
			}

			System.out.println(answer);
		}

	}
	
	static long sumFactDigits(int j){
		
		int p;
		
		int out = 0;
		
		while(j > 0){
			
			p=j%10;
			
			j=j/10;
			
			out+=fact(p);
			
		}
		
		return out;
		
	}
	
	static long fact(int j){
		
		long out = 1;
		
		for(int p = 1; p <= j; p++){
			
			out*=p;
			
		}

		return out;
		
	}

}
