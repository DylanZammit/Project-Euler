
public class Problem32 {
	
	static int[] digits = new int[10];
	static boolean add = true;
	static boolean added = false;
	static long out = 0;

	public static void main(String[] args) {

		for(int i = 1; i < 1000000; i++){
			getFactors(i);
			added = false;
		}
		System.out.println(out);

	}
	
	public static void setZero(){
		
		for(int i = 0; i < digits.length; i++){
			digits[i]=0;
		}
		
	}
	
	public static void getFactors(int x){

		int prodLength = (int)(Math.log10(x)+1);
		int aLength, bLength, totLength;
		
		int max = (int)(Math.sqrt(x));
		
		for(int i = 2; i <= max && !added; i++){
			
			setZero();
			
			add = true;
			
			if(x%i==0){

				aLength = (int)(Math.log10(i)+1);
				bLength = (int)(Math.log10(x/i)+1);
				
				totLength = aLength + bLength + prodLength;
				
				
				if(totLength == 9){
					
					int[] nums = {x, i, x/i};
					
					for(int k = 0; k < nums.length && add; k++){
						
						int temp = nums[k];
						int len = (int)(Math.log10(temp)+1);
						for(int j = 0; j < len && add; j++){

							if(digits[temp%10]==1 || temp%10 == 0){
								add = false;
							}else{
								digits[temp%10]=1;
							}
							
							temp/=10;
							
						}
						
					}
					
					
					if(add){
						out+=x;
						added = true;
					}
					
				}
			}
			
		}
		
	}

}
