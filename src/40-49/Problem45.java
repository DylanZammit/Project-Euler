
public class Problem45 {

	public static boolean found = false;
	
	public static void main(String[] args) {

		for(int i = 40756; !found; i++){
			
			//can ignore triangle numbers since they are also hexagonal numbers
			if(/*t(i) && */p(i) && h(i)){
				found = true;
				System.out.println(i);
			}
			
		}

	}
	
	public static boolean t(int x){
		return((-1+Math.sqrt(1+(double)8*x))/2%1==0)?true:false;
	}
	
	public static boolean p(int x){
		return((1+Math.sqrt(1+(double)24*x))/6%1==0)?true:false;
	}

	public static boolean h(int x){
		return((1+Math.sqrt(1+(double)8*x))/4%1==0)?true:false;
	}
	

}
