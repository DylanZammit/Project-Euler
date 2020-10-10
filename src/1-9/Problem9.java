
public class Problem9 {
	
	static int a, b, c;
	
	static boolean solved = false;
	
	static int sum;
	
	public static void main(String[] args) {
		
		
		for(int q = 1; !solved ; q+=2){
			sum = 0;
			for(int p = 1; sum < 1000; p+=2){
				a=p*q;
				b=(p*p-q*q)/2;
				c=(p*p+q*q)/2;
				
				sum = a+b+c;
				
				if(sum==1000){
					System.out.println(a*b*c);
					solved = true;
				}
				
			}
			
		}

	}

}
