
public class Problem53 {

	static int answer = 0;
	
	public static void main(String[] args) {
		
		for(int n = 23; n <= 100; n++){
			
			for(int r = 2; r <= n/2; r++){
				
				if(getComb(n, r)>1000000){
					
					if(2*r==n){
						answer++;
					}else{
						answer+=2;
					}
					
				}
				
			}
			
		}
		
		System.out.println(answer);

	}

	public static double getComb(int n, int r){
		
		return Math.pow(n,  (n+(float)1/2))/(Math.sqrt(2*Math.PI)*Math.pow(r, (r+(float)1/2))*Math.pow(n-r, (n-r+(float)1/2)));
	}
	
}
