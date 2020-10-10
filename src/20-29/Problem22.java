import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class Problem22 {

	static String[] nameList;
	
	static final String filename = "Problem22.txt";
	static String line = null;
	
	static long answer = 0;
	
	public static void main(String[] args) {

		inputNames();
		
		for(int i = 0; i < nameList.length; i++){
			
			answer+=((getCode(nameList[i])*(i+1)));
		}
		
		System.out.println(answer);

	}
	
	static long getCode(String name){
		
		int out = 0;
		
		for(int j = 0; j < name.length(); j++){
			
			out+=((int)name.charAt(j) - 64);
			
		}
		
		return out;
		
	}

	static void inputNames(){
		
		try{
			 
	           FileReader fileReader = new FileReader(filename);

	           BufferedReader bufferedReader = new BufferedReader(fileReader);

	           int j = 0;
	           
	           String temp = "";
	           
	           while((line = bufferedReader.readLine()) != null) {
	               
	        	   temp+=line;
	           }  
	           
	           nameList = temp.split("\",\"");
	           Arrays.sort(nameList);
	           
	           bufferedReader.close();         
	       }catch(FileNotFoundException ex) {
	           System.out.println("Unable to open file '" + filename + "'");                
	       }catch(IOException ex) {
	           ex.printStackTrace();
	       }
		
	}
	
}
