
public class Problem43 {

	static int[] a = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
	static int[] prime = {2, 3, 5, 7, 11, 13, 17};
	static long[] list = new long[3628800];
	
	static long answer;
	
	static boolean found = true;
	
	public static void main(String[] args) {

		permute(0, a);

		for(int i = 0; i < list.length; i++){

			for(int j = 1; j<=7 && found; j++){
				
				String s="";
				
				if((int)(Math.log10(list[i])+1)==9){
					
					s="0";
					
				}
				
				s+=Long.toString(list[i]);
				
				int subNum = Integer.parseInt(s.substring(j, j+3));

				if(subNum%prime[j-1]!=0){
					found = false;
				}
				
			}
			
			if(found){
				answer+=list[i];
			}else{
				found = true;
			}
			
		}
		
		System.out.println(answer);
		
	}
	
	

	static int c = 0;
	public  static void permute(int start, int[] input ) {
        if (start == input.length) {
        	String num = "";
            for(int x: input){
            	num+=x;
	        }

            long out = Long.parseLong(num);
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
