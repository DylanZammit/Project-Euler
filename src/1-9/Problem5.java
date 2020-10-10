
public class Problem5 {

	static int num = 20;
	
	public static void main(String[] args) {
		
		int count = 1;
		int current;
		boolean isAns = false;
		
		while(!isAns){
			//System.out.println(count);
			current = num*count;
			isAns = true;
			for(int i = 19; i > 10 && isAns; i--){
				
				if(current%i!=0){
					isAns = false;
				}
				
			}
			
			if(isAns){
				System.out.println(current);
			}
			
			count++;
		}

	}

}
