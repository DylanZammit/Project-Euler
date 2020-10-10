
public class Problem38 {
	
	static int[] a = {9, 8, 7, 6, 5, 4, 3, 2, 1};
	static int[] list = new int[362880];
	
	public static boolean found = false;

	public static void main(String[] args) {

		permute(0, a);
		
		int ansIndex = 0;
		
		while(!found){
			
			canCon(ansIndex);
			
			ansIndex++;
			
		}

	}
	
	public static void canCon(int x){
		
		String num = Integer.toString(list[x]);
		
		for(int i = 1; i <= 8 && !found; i++){
			
			String currStr = num.substring(0, i);
			int currNum = Integer.parseInt(currStr);
			
			int accum = currStr.length();
			
			int mult = 2;
			
			String toFind;
			
			while(accum < 9 && !found){
				
				toFind = Integer.toString(mult*currNum);

				accum+=toFind.length();

				if(accum <= 9 && toFind.compareTo(num.substring(accum-toFind.length(), accum)) == 0){

					System.out.println(toFind + " " + mult + " " + accum);
					if(accum == 9){
						found = true;
						System.out.println(num);
						
					}
					
				}else{
					break;
				}
				
				mult++;
				
			}
			
		}
	}

	static int c = 0;
	public  static void permute(int start, int[] input ) {
        if (start == input.length) {
        	String num = "";
            for(int x: input){
            	num+=x;
	        }
            
            int out = Integer.parseInt(num);
            list[c] = out;
            c++;
            
	        return;
	    }
	    for (int i = start; i < input.length; i++) {
	
	        int temp = input[i];
	        input[i] = input[start];
	        input[start] = temp;
	
	        permute(start + 1, input);
	        
	        int temp2 = input[i];
	        input[i] = input[start];
	        input[start] = temp2;
	    }
	}
	

}
