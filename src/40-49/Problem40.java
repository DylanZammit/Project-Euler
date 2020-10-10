
public class Problem40 {

	static String num;
	
	static int answer = 1;
	
	static int count = 0;

	static int inCt = 0;
	
	static int dig;
	
	static double cap = Math.pow(10, inCt);
	
	public static void main(String[] args) {

		for(int i = 1; i < 200000; i++){

			count+=(int)(Math.log10(i)+1);
			
			if(count >= cap){
				
				num = Integer.toString(i);
				
				dig = Character.getNumericValue(num.charAt((int) (num.length() - 1 - (count-cap))));
				
				answer*=dig;
				inCt++;
				cap = Math.pow(10, inCt);
			}
			
		}
		
		System.out.println(answer);
		

	}

}
