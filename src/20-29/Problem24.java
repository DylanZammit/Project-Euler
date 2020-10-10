import java.util.ArrayList;
import java.util.Collections;

public class Problem24 {
	
	static int count = 0;

	static ArrayList<Long> list = new ArrayList();

	static int digits[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	public static void main(String[] args) {

		perm(0, digits.length-1);
			
		Collections.sort(list);

		System.out.println(list.get(1000000-1));

	}
	
	static void perm(int i, int n){
		
		if(i==n){

			long store = 0;
			
			for(int x = 0; x <= n; x++){
				
				store*=10;
				store+=digits[x];
				
			}
				
			list.add(store);
			
		}else{
			
			for(int j = i; j <= n; j++){
				
				swap(i, j);
				perm(i+1, n);
				swap(j, i);
			}
			
		}
		
	}
	
	static void swap(int p, int q){
		
		int x = digits[p];
		digits[p]=digits[q];
		digits[q]=x;
		
	}

}
