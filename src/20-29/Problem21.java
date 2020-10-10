
public class Problem21 {
	

	public static void main(String[] args) {

		System.out.println(getAnswer());
		
	}
	
	static long getAnswer(){

		long answer = 0;
		for(int i = 1; i < 10000; i++){
			
			long temp = sumDiv(i);

			if(i == sumDiv(temp) && i != temp){
				
				answer+=temp;
				
			}
		}
		
		return answer;
	}
	
	static long sumDiv(long i){
		
		int tempRt = (int)Math.sqrt(i);
		
		int out = 1;
		
		for(int p = 2; p <= tempRt; p++){
			
			if(i%p==0){

				out+=p;
				out+=(i/p);
				
			}
			
		}
		
		return out;
		
		
	}

}
