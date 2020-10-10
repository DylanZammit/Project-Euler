
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;

public class Problem70 {

	static HashSet<Integer> primFacts = new HashSet<>();

	static double min = -1;
	static int answer;

	static int currTotSize;
	static int nSize;
	
	static int currTot;
	
	public static void main(String[] args) {

		for(int n = 2; n < 1e7; n++){

			PrimeFactors.getPrimeFactors(n);
			primFacts = PrimeFactors.factors;
			
			currTot = tot(n);

			currTotSize = NumberLength.getSize(currTot);
			nSize = NumberLength.getSize(n);
			
			if(currTotSize == nSize){
				if(arePerms(currTot, n)){
					if((double)n/currTot < min || min == -1){
						min = (double)n/currTot;
						answer = n;
					}
				}
			}

			primFacts.clear();
		}

		System.out.println(answer);

	}
	
	static boolean arePerms(int a, int b){

		int[] digitsA = new int[nSize];
		int[] digitsB = new int[nSize];
		
		for(int i = 0; i < nSize; i++){
			digitsA[i] = a%10;
			digitsB[i] = b%10;
			a/=10;
			b/=10;
		}

		Arrays.sort(digitsA);
		Arrays.sort(digitsB);
		
		return (Arrays.equals(digitsA, digitsB))?true:false;
		
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
