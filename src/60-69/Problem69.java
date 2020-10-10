import java.util.HashSet;
import java.util.Iterator;

public class Problem69 {

	static int answer;

	static double max = 0;
	
	static HashSet<Integer> primFacts = new HashSet<>();
	
	public static void main (String[] args){
		
		for(int n = 2; n <= 1000000; n++){
			PrimeFactors.getPrimeFactors(n);
			primFacts = PrimeFactors.factors;
			
			int currTot = tot(n);
			
			if((double)n/currTot > max){
				max = (double)n/currTot;
				answer = n;
			}

			primFacts.clear();
		}

		System.out.println(answer);
		
	}
	
	static int tot(int n){
		
		double out = n;
		
		Iterator<Integer> iter = primFacts.iterator();
		
		while(iter.hasNext()){
			int p = iter.next();
			out*=(1-(double)1/p);
		}
		
		return (int)out;
		
	}

}
