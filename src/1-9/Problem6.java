
public class Problem6 {

	public static void main(String[] args) {
		
		int n = 100;
		int answer = 0;
		
		for(int i=2; i<=n; i++){
			
			answer+=i*triNum(i-1);
			
		}
		
		answer*=2;
		System.out.println(answer);

	}
	
	static long triNum(int n){
		int out = 0;
		for(int i = 0; i <= n; i++){
			out+=i;
		}
		return out;
	}

}
