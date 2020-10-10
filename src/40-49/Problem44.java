public class Problem44 {

	static boolean found = false;
	
	public static void main(String[] args) {

		for(int i = 2; !found; i++){
			
			int currPen = getPen(i);
			
			for(int j = 1; j < i; j++){
			
				int secPen = getPen(j);
				
				if(isPen(currPen+secPen) && isPen(currPen-secPen)){
					System.out.println(currPen-secPen);
					found = true;
				}
			}
		}
	}
	
	public static boolean isPen(int n){
		return ((1+Math.sqrt(1+24*n))/6%1==0)?true:false;
	}

	public static int getPen(int n){
		return n*(3*n-1)/2;
	}

}
