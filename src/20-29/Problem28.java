
public class Problem28 {
	
	static long answer = 1;
	static int dims = 3;
	static long currNum = 1;
	
	public static void main(String[] args) {
		
		int adder = dims-1;
		int counter = 0;
		
		while(dims <= 1001){
			
			counter++;
			
			currNum+=adder;
			
			answer+=currNum;
			
			if(counter%4==0){
				counter = 0;
				dims+=2;
				adder+=2;
			}
			
		}
		
		System.out.println(answer);

	}

}
