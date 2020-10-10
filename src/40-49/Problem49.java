import java.util.ArrayList;

public class Problem49{

	static ArrayList<Integer> primes = new ArrayList<>();
	
	public static void main(String[] args) {
		
		for(int i = 1000; i < 10000;i++){
			
			if(Functions.isPrime(i)){
				primes.add(i);
				
			}
			
		}
		
		for(int jump = 2; jump < 5000; jump++) {

			for(int i = 0; i < primes.size() && primes.get(i) + jump*2 < 10000; i++) {

				int num1 = primes.get(i);
				int num2 = num1+ jump;
				int num3 = num2 + jump;
				
				int[] input = {num1, num2, num3};
				
				if(primes.contains(num2) && primes.contains(num3) && samePerms(input)) {
					System.out.println(jump + ":  " +num1 + " " + num2 + " " + num3);
				}
				
			}
		}
		
	}
	
	static boolean samePerms(int[] a) {
		
		if(Functions.getPermForm(a[0]) == Functions.getPermForm(a[1]) && Functions.getPermForm(a[1]) == Functions.getPermForm(a[2])) {
			return true;
		}
		
		return false;
	}

}
