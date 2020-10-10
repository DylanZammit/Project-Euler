
public class Problem12 {
	
	static boolean solved = false;

	static long n = 1;
	static long tri = 0;
	static long temp;
	static long count;
	
	public static void main(String[] args) {

		while(!solved){
			tri+=n;
			count = 0;

			temp=(long)Math.sqrt(tri);
			
			for(int i = 1; i<=temp; i++){
				if(tri%i==0){
					count++;
				}
			}
			
			count=count*2-1;
			
			if(count>500){
				solved=true;
			}
			
			n++;
		}
		
		System.out.println(tri);
		
	}

}
