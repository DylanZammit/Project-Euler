
public class Problem63 {

	static boolean stop = false;
	
	public static void main(String[] args) {

		int size;
		
		int count = 0;
		
		for(int i = 1; true; i++){
			
			
			for(int j = 1; !stop; j++){
				
				size = getSize(Math.pow(j, i));
				
				if(size==i){
					count++;
					System.out.println(count);
				}
				
				if(size > i){
					stop = true;
				}
				
			}
			
			stop = false;
			
		}

	}
	
	static int getSize(double x){
		return (int) Math.log10(x) + 1;
	}

}
