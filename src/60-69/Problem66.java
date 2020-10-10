
public class Problem66 {

	static boolean found;
	
	static double max = 0;
	
	final static int maxD = 1000;
	static int answer = 0;
	
	public static void main(String[] args) {

		for(int D = 2; D <= maxD; D++){

			found = false;
			if(!isSquare(D)){
				
				double x = 1;
				
				double y;
				
				while(!found){
					x++;
					
					y = Math.sqrt((double)(x*x-1)/D);
					if(isInteger(y) && y > 0){
						//System.out.println(y);
						if(x > max){
							//System.out.println(D);
							max = x;
							answer = D;
						}
						
						found = true;
					}
					
				}
				
				
			}
			
			//System.out.println(max);
		}
		
		System.out.println(max + " " + answer);

	}
	
	static boolean isSquare(long D){
		return (Math.sqrt(D)%1==0)?true:false;
	}
	
	static boolean isInteger(double x){
		return (x%1==0)?true:false;
	}

}
