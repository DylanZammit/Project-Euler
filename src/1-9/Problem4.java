
public class Problem4 {

	static int upper = 999;
	static int lower = 100;
	
	static int count = upper*upper;
	
	public static void main(String[] args) {
	
		boolean finished = false;
		
		while(count > lower*lower && !finished){
			if(isPal(count)){
				if(has3digfacs(count)){
					System.out.println(count);
					finished = true;
				}
			}
			count--;
		}
		
	}
	
	static boolean has3digfacs(int i){
		
		for(int div = upper; div >= lower; div--){
			if(i%div==0 && i/div>=lower && i/div<=upper){
				return true;
			}
		}
		
		return false;
		
	}
	
	static boolean isPal(int i){
		
		String temp = Integer.toString(i);
		
		int size = temp.length();
		
		int lp = 0;
		int rp = size-1;
		
		while(lp < rp){
			if(temp.charAt(lp) != temp.charAt(rp)){
				return false;
			}
			lp++;
			rp--;
		}
		
		return true;
		
	}
}
