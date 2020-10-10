
public class Problem92 {
	
	static int answer = 0;

	public static void main(String[] args) {

		for(long i = 2; i < 10000000; i++){
			
			if(sqn(i)){
				
				answer++;
				
			}
		}
		System.out.println(answer);

	}
	
	static boolean sqn(long i){
		
		while(true){

			i = getSqDig(i);

			if(i == 89){
				return true;
			}else if(i == 1){
				return false;
			}
			
		}
		
		
	}
	
	static long getSqDig(long t){
		
		long out = 0;
		
		long temp;
		
		while(t>0){
			
			temp = t%10;
			
			t/=10;
			
			out+=(temp*temp);
			
		}
		
		return out;
		
	}

}
