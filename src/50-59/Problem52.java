import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Problem52 {

	static boolean found = false;
	
	static boolean inner = false;
	
	final static int maxMult = 6;

	static ArrayList<Integer> orig = new ArrayList<>();
	static ArrayList<Integer> comp = new ArrayList<>();
	
	public static void main(String[] args) {
		
		int length, length6;
		
		for(int i = 100; !found; i++){
		//int i = 125874;
			length = (int)(Math.log10(i)+1);

			length6 = (int)(Math.log10(i*maxMult)+1);

			inner = true;
			
			if(length==length6){
				storeDigits(i, orig);
				
				for(int j = 2; j <= maxMult && inner; j++){
					
					storeDigits(i*j, comp);
					
					if(!checkDigits()){
						
						inner = false;
						
					}
					comp.clear();
					
				}
				
				if(inner){
					found = true;
					System.out.println(i);
				}
				
			}
			
			orig.clear();
			comp.clear();
			
		}
			

	}
	
	public static boolean checkDigits(){
		
		for(int i = 0; i < comp.size(); i++){

			//System.out.println(x + " " + x%10);
			if(comp.get(i) != orig.get(i)){
				return false;
			}
			
		}
		
		return true;
		
	}
	
	public static void storeDigits(int x, ArrayList<Integer> y){
		
		while(x>0){
			
			y.add(x%10);
			x/=10;
			
		}
		
		Collections.sort(y);

	}

}
