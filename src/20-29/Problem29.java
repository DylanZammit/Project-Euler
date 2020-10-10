import java.util.HashSet;

public class Problem29 {
//9183
	
	public static void main(String args[]){
		
		int n = 99;
		
		double[] elements = new double[n*n];
		int counter = 0;
		for(int i = 2; i <=n+1; i++ ){
			for(int j = 2; j <= n+1; j++){
				double mult = Math.pow(i,j);

				elements[counter] = mult;
				counter++;
			}
		}
		
		HashSet<Double> hs = new HashSet<Double>();
		
		for(int p = 0; p < counter; p++){

			if(!hs.contains(elements[p])){
				hs.add(elements[p]);
			}

		}
		System.out.println(hs.size());
	}


}
