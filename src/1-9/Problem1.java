
public class Problem1 {
	
	public static void main(String args[]){
		
		long answer = 0;
		
		for(int i=0; i < 1000; i++){
			if(i%3==0 || i%5==0)
				answer+=i;
		}
		
		System.out.println(answer);
	}

}
