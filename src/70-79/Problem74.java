import java.util.HashSet;

public class Problem74 {

	static double[] start = {145, 169, 363601, 1454, 871, 45361, 872, 45362};
	
	static HashSet<Double> repList = new HashSet<>();
	
	static int answer = 0;
	
	public static void main(String[] args) {

		
		
		for(int i = 0; i < start.length; i++){
			repList.add(start[i]);
		}
		
		for(int n = 2; n < 1e6; n++){
			if(numTerms(n)==60){
				answer++;
			}
		}

		System.out.println(answer);

	}
	
	static int numTerms(int n){
		
		int count = 0;
		
		double nextTerm = n;
		
		while(count < 60){

			count++;
			
			if(repList.contains(nextTerm)){
				
				if(nextTerm == 169 || nextTerm == 363601 || nextTerm == 1454){
					return count+=2;
				}else{
					return count+1;
				}
			}
			
			nextTerm = nextTerm(nextTerm);
			
			
		}
		
		return -1;
		
	}
	
	static double nextTerm(double x){
		
		double out = 0;
		
		while(x > 0){
			
			out+=fact(x%10);
			x = (x-x%10)/10;
			
		}
		
		return out;
		
	}
	
	static double fact(double x){
	
		if(x == 0){
			return 1;
		}
		
		double out = 1;
		
		for(int i = 1; i <=x; i++){
			out*=i;
		}
		
		return out;
		
	}

}
