
public class Problem85 {

	static long diff = 1000000000;
	
	static long answer;
	
	static int target = 2000000;
	
	public static void main(String[] args) {

		for(int a = 1; true; a++){
			
			int v = a*(a+1);
			
			long b = (long)Math.round((-v+Math.sqrt(v*v+(double)4*4*v*target))/(2*v));

			long numRects = a*b*(a+1)*(b+1)/4;

			if(Math.abs(target-numRects) < diff){

				diff = Math.abs(target-numRects);
				
				if(a*b!=0){
					answer = a*b;
					System.out.println(answer+ "...."+a+"x"+b + "...." + numRects + " " + diff);
				}
			}
			
			b++;
			
			numRects = a*b*(a+1)*(b+1)/4;
			
			if(Math.abs(target-numRects) < diff){

				diff = Math.abs(target-numRects);
				
				if(a*b!=0){
					answer = a*b;
					System.out.println(answer+ "...."+a+"x"+b + "...." + numRects + " " + diff);
				}
			}
			
		}

	}

}
