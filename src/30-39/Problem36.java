
public class Problem36 {

	static int answer = 0;
	
	public static void main(String[] args) {
		
		for(int i = 1; i < 1000000; i++){
			
			if(checkPal(Integer.toString(i)) && checkPal(Integer.toBinaryString(i))){
				
				answer+=i;
				
			}
			
		}

		System.out.println(answer);
		
	}
	
	public static boolean checkPal(String x){
		
		int lc = 0;
		int rc = x.length()-1;
		
		while(lc < rc){
			
			if(x.charAt(lc) != x.charAt(rc)){
				
				return false;
				
			}
			
			lc++;
			rc--;
		}
		
		return true;
		
	}

}
