import java.io.*;
import java.util.ArrayList;
import java.math.BigInteger;

public class Problem13 {

	static BigInteger[] numList = new BigInteger[100];
	
	static BigInteger answer = BigInteger.ZERO;
	
	static final String filename = "Problem13.txt";
	
	static String line = null;
	
	public static void main(String[] args) {

		inputString();
		
		getAnswer();
		
		System.out.println(answer);
		
		
	}
	
	static void getAnswer(){
		
		for(int i = 0; i < numList.length; i++){
			answer = answer.add(numList[i]);
			
		}
		
	}

	static void inputString(){
		
		 try{
		 
           FileReader fileReader = new FileReader(filename);

           BufferedReader bufferedReader = new BufferedReader(fileReader);

           int j = 0;
           
           while((line = bufferedReader.readLine()) != null) {
               
        	   numList[j] = new BigInteger(line);
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
