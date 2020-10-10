
public class Problem33 {
	
	static int[] nums = new int[4];
	
	static double answer = 1;
	
	public static void main(String[] args) {
		
		double digd1, digd2, dign1, dign2;
		
		boolean trivial;
		
		double badFr = 0;
		
		for(double denom = 10; denom < 100; denom++){
			
			trivial = false;
			
			digd1 = (int)denom%10;
			digd2 = (int)denom/10;
			
			for(double numer = 10; numer < denom; numer++){
				
				dign1 = (int)numer%10;
				dign2 = (int)numer/10;
				
				trivial = (digd1==dign1)?true:false;
				
				badFr = 0;
				
				if(!trivial){
					if(digd1 == dign1 && digd2 != 0){
						badFr = dign2/digd2;
					}else if(digd1 == dign2 && digd2 != 0){
						badFr = dign1/digd2;
					}else if(digd2 == dign1 && digd1 != 0){
						badFr = dign2/digd1;
					}else if(digd2 == dign2 && digd1 != 0){
						badFr = dign1/digd1;
					}
					
					if(badFr == numer/denom){
						System.out.println((int)numer + "/" + (int)denom);
						answer*=badFr;
					}
					
				}
			}
			
		}
		

	}

}
