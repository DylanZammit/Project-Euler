
public class Problem46 {

	public static void main(String[] args) {

		System.out.println(getNum());

	}
	
	static int getNum(){
		
		for(int i = 100; true; i++){
			
			if(!isGold(i)){
				return i;
			}
			
			
		}
		
	}
	
	static boolean isGold(int i){
		if(!Functions.isPrime(i)){
			for(int j = (int)Math.sqrt(i); j >= 1; j--){
				int fun = i - 2*j*j;

				if(fun > 0){
					if(Functions.isPrime(fun)){
						return true;
					}
				}
				
			}
			
			return false;
		}else{
			return true;
		}
	}

}
