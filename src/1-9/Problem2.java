
public class Problem2 {

	static long answer = 0;
	
	public static void main(String[] args) {

		fibb(0, 1);
		System.out.println(answer);

	}
	
	static void fibb(int i, int j){
		if(j%2==0){
			answer+=j;
		}
		if(j < 4000000){
			fibb(j, i+j);
		}
		
	}

}
