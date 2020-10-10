
public class Problem30 {
	
	static long answer = 0;

	public static void main(String[] args) {
		
		long temp;
		
		for(int i = 2; true; i++){
			
			temp = digitPowSum(i);
			
			
			if(temp == i){
				
				answer+=i;
				System.out.println(answer);
			}
			
		}
		

	}
	
	public static long digitPowSum(int in){
		
		int length = (int)(Math.log10(in)+1);
		
		int out = 0;
		
		double currentMod;
		
		for(int i = 0; i < length; i++){

			currentMod = in%10;
			in/=10;
					
			out+=Math.pow(currentMod, 5);
			
		}
		
		return out;
		
	}
	

}
