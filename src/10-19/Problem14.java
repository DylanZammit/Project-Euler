
public class Problem14 {
	
	static long tempNum;
	static long chainCount;
	static long largest = 0;
	static long answer;
	
	public static void main(String[] args) {

		long startTime = System.currentTimeMillis();

		for(int n = 2; n < 1000000; n++){
			
			tempNum = n;
			chainCount = 0;
			
			while(tempNum != 1){
				
				if(tempNum%2 == 0){
					tempNum/=2;
				}else{
					tempNum=tempNum*3+1;
				}
				
				chainCount++;
				
			}
			
			
			if(chainCount>largest){
				largest = chainCount;
				answer = n;
			}
		}
		
		System.out.println(answer);

		long endTime = System.currentTimeMillis();
		float duration = (float)((endTime - startTime)/1000f);
		
		System.out.println(duration);
	}

}
