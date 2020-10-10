import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Problem11 {

	static String[][] inputList = new String[20][20];
	static int[][] input = new int[20][20];
	
	static final String filename = "Problem11.txt";
	static String line = null;
	
	static int answer = 1;
	
	static int temp;
	
	public static void main(String[] args) {

		inputData();
		convertToInt();

		checkColumns();
		checkRows();
		checkDiagsRight();
		checkDiagsLeft();
		
		System.out.println(answer);
		
	}
	
	static void checkColumns(){
		
		for(int i = 0; i < 20; i++){
			
			for(int j = 0; j < 17; j++){
				
				temp=input[i][j]*input[i][j+1]*input[i][j+2]*input[i][j+3];

				if(temp > answer){
					
					answer = temp;
					
				}
			}
		}
	}
	
	static void checkRows(){
		
		for(int i = 0; i < 17; i++){

			for(int j = 0; j < 20; j++){
				
				temp=input[i][j]*input[i+1][j]*input[i+2][j]*input[i+3][j];

				if(temp > answer){
					
					answer = temp;
					
				}
			}
		}
	}
	
	static void checkDiagsRight(){
		
		for(int i = 0; i < 17; i++){
			
			for(int j = 0; j < 17; j++){
				
				temp=input[i][j]*input[i+1][j+1]*input[i+2][j+2]*input[i+3][j+3];

				if(temp > answer){
					
					answer = temp;
					
				}
			}
		}
	}

	static void checkDiagsLeft(){
		
		for(int i = 3; i < 20; i++){
			
			for(int j = 0; j < 17; j++){
				
				temp=input[i][j]*input[i-1][j+1]*input[i-2][j+2]*input[i-3][j+3];

				if(temp > answer){
					
					answer = temp;
					
				}
			}
		}
	}
	static void convertToInt(){
		
		for(int i = 0; i < inputList.length; i++){
			
			for(int j = 0; j < inputList[0].length; j++){
				
				input[i][j] = Integer.parseInt(inputList[i][j]);
				
			}
			
		}
		
	}
	
	static void inputData(){
		
		try{
			 
	           FileReader fileReader = new FileReader(filename);

	           BufferedReader bufferedReader = new BufferedReader(fileReader);

	           int j = 0;
	           
	           while((line = bufferedReader.readLine()) != null) {
	               
	        	   inputList[j] = line.split(" ");
	        	   
	        	   j++;
	           }  

	           bufferedReader.close();         
	       }catch(FileNotFoundException ex) {
	           System.out.println("Unable to open file '" + filename + "'");                
	       }catch(IOException ex) {
	           ex.printStackTrace();
	       }
		
	}

}
