import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Problem41 {
	
	static ArrayList<Integer> list = new ArrayList();

	static int digits[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	//static int digits[] = {1, 2, 3, 4};
	static int temp[];
	
	public static void main(String[] args) {

		boolean found = false;
		
		for(int i = 0; i <= digits.length; i++){
			
			temp = digits;
			temp = Arrays.copyOf(temp, temp.length-i);

			perm(0, temp.length-1);
			
		}
		
		Collections.sort(list);

		for(int j = list.size()-1; j >= 0 && !found; j--){
			
			int num = list.get(j);

			if(isPrime(num)){

				if(isPan(num)){

					System.out.println(num);
					found = true;
				}
				
			}
			
		}
		
		
	
	}
	
	static void perm(int i, int n){
		
		if(i==n){

			int store = 0;
			
			for(int x = 0; x <= n; x++){
				
				store*=10;
				store+=temp[x];
				
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
		
		int x = temp[p];
		temp[p]=temp[q];
		temp[q]=x;
		
	}

	static boolean isPrime(int j){
		
		int temp = (int) Math.sqrt(j);
		
		for(int k = 3; k <= temp; k++){
			
			if(j%k==0){
				
				return false;
			}
			
		}
		
		return true;
		
	}
	
	static boolean isPan(int j){
		
		String num = Integer.toString(j);
		
		
		for(int i = 1; i <= num.length(); i++){
			
			if(!num.contains(Integer.toString(i))){
				return false;
			}
			
		}
		
		
		return true;
		
	}

}
