
public class Problem39 {
	
	static int largest = 0;
	
	static int answer = 0;
	
	public static void main(String[] args) {
		
		for(int p = 5; p <= 1000; p++){
			
			int ways = totWays(p);

			if(ways > largest){
				
				largest = ways;
				answer = p;
				
			}
			
		}
		
		System.out.println(answer);

	}
	
	static int totWays(int n){
		
		int out = 0;
		int a = 0;
		int b = 0;
		int c = 0;
		
		for(int p = 3; (a+b+c)/2<n;p+=2){
			
			for(int q = 1; q<p;q+=2){
				a = p*q;
				b = (p*p-q*q)/2;
				c = (p*p+q*q)/2;
				
				int sum = a+b+c;
				
				if(n%sum==0){
					
					out++;
					
				}
				
			}
			
		}
		
		return out;
		
	}

}
