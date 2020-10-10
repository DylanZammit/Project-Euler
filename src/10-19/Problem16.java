import java.util.ArrayList;

public class Problem16 {

	static int n = 1;
	
	static boolean carry;
	
	static int currDig;
	
	static ArrayList<Integer> digits = new ArrayList<Integer>();
	
	static int currentSize;
	
	static int answer = 0;
	
	public static void main(String[] args) {

		digits.add(n);
		
		for(int n = 1; n <= 1000; n++){
			
			currentSize = digits.size();
			
			carry = false;
			
			for(int i = 0; i <= currentSize; i++){
				
				if(i == currentSize){
					
					if(carry){
						digits.add(1);
					}
					
				}else{
				
					if(!carry){
						currDig = digits.get(i)*2;
						
					}else{
						currDig = digits.get(i)*2+1;
					}
					
					if(currDig>=10){
						
						digits.set(i, currDig%10);
						
						carry = true;
						
					}else{
						
						digits.set(i, currDig);
						
						carry = false;
						
					}
				}
				
			}
			
		}
		
		for(int i = 0; i < digits.size(); i++){
			answer+=digits.get(i);
		}
		
		//display 2^1000
		dispArr();
	}
	
	static void dispArr(){
		for(int i = digits.size()-1; i >=0; i--){
			
			System.out.print(digits.get(i));
			
		}
		System.out.println();
	}
	

}
