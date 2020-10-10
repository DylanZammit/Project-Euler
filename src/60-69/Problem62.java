import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Problem62 {
	
	static boolean found = false;
	
	static int oddCount = 0;

	static int size;
	
	static double currNum;
	
	static HashSet<BigInteger> power = new HashSet<>();
	
	static HashSet<Integer> checked = new HashSet<>();
	
	static ArrayList<BigInteger> dubles = new ArrayList<>();
	
	static int[] digits;

	static final int numOfPerms = 5;
	
	public static void main(String[] args) {

		BigInteger digComb = BigInteger.ZERO;
		
		BigInteger currNum;
		
		for(int i = 5; !found; i++){
			currNum = BigInteger.valueOf(i).pow(3);
			
			digComb = getLowestPerm(currNum);
			if(!power.contains(digComb)){
				power.add(digComb);
			}else{
				dubles.add(digComb);
				if(Collections.frequency(dubles, digComb) == numOfPerms-1){
					found = true;
				}
			}
			
			
		}
		
		int cube = getLowestCube(digComb);

		System.out.println(cube);
		System.out.println(BigInteger.valueOf(cube).pow(3));

	}
	
	static int getLowestCube(BigInteger x){
		
		BigInteger currtemp;
		
		for(int i = 1; true; i++){
			
			currtemp = getLowestPerm(BigInteger.valueOf(i).pow(3));
			
			if(x.compareTo(currtemp)==0){
				return i;
			}
			
		}
		
	}
	
	static BigInteger getLowestPerm(BigInteger x){
		ArrayList<Integer> tempDig = new ArrayList<>();
		
		int digit;
		
		while(x.compareTo(BigInteger.ZERO) == 1){
			digit = x.mod(BigInteger.TEN).intValue();
			tempDig.add(digit);
			x=x.divide(BigInteger.TEN);
		}
		
		Collections.sort(tempDig, Collections.reverseOrder());
		
		BigInteger out = BigInteger.ZERO;
		
		for(int j = 0; j < tempDig.size(); j++){
			out = out.multiply(BigInteger.TEN);
			out=out.add(BigInteger.valueOf(tempDig.get(j)));
		}
		
		return out;
		
		
	}
	
	static int getSize(double x){
		return (int) Math.log10(x) + 1;
	}
	

}
