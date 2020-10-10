public class Problem51 {

	static boolean found = false;
	
	final static int familyNum = 8;
	
	static int familyCount;
	
	public static void main(String[] args) {

		int maxDig = 10-familyNum;
		
		int ind;
		
		String numStr;
		
		int repCt = 0;
		
		for(int i = 2; !found; i++){

			familyCount = 0;
			
			if(isPrime(i)){
				
				familyCount++;
				
				numStr = Integer.toString(i);
				
				for(int a = 0; a <= maxDig && familyCount != familyNum; a++){
					
					familyCount=1;
					
					char currDig = Character.forDigit(a, 10);
					
					ind = numStr.indexOf(currDig);
					repCt=0;
					while(ind >= 0 && ind != numStr.length()-1) {
						repCt++;
					    ind = numStr.indexOf(currDig, ind+1);
					}
					
					if(repCt >= 2){
						
						String repStr;
						
						for(int j = a+1; j <= 9; j++){
							
							char digRep = Character.forDigit(j, 10);
							
							repStr = numStr.replace(Character.toString(currDig), Character.toString(digRep));
							
							if(isPrime(Integer.parseInt(repStr))){

								familyCount++;
								
							}
							
							
						}
						
					}
					
				}
				
			}
			if(familyCount == familyNum){
				found = true;
				System.out.println(i);
			}
			
		}

	}
	
	public static boolean isPrime(int x){
		
		int temp = (int)Math.sqrt(x);
		
		
		for(int i = 2; i <= temp; i++){
			
			if(x%i==0){
				return false;
			}
			
		}
		
		return true;
		
	}


}
