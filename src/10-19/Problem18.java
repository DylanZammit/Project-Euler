import java.util.ArrayList;
import java.io.*;

public class Problem18 {

	static int numRows = 0;
	static int rowElements;
	
	static final String filename = "Problem18.txt";
	static String line = null;
	
	static ArrayList<Integer> triNums = new ArrayList<Integer>();

	static ArrayList<Integer> treeList = new ArrayList<Integer>();
	
	static ArrayList<Integer>[] temp;
	
	
	public static void main(String[] args) {
		
		
		inputNums();

		temp = new ArrayList[numRows];
		
		initArr();
		
		treeStore(0, 1);
		
		for(int i = 0; i < temp.length; i++){
			for(int j = 0; j < temp[i].size(); j++){
				treeList.add(temp[i].get(j));
			}
		}
		
		System.out.println(getShortest());
		
	}
	
	static void initArr(){
		for(int i = 0; i < temp.length; i++){

			temp[i] = new ArrayList<Integer>();
		}
	}
	
	static void treeStore(int i, int rowNum){

		temp[rowNum-1].add(triNums.get(i));
		
		if(rowNum < numRows){
			treeStore(i+rowNum, rowNum+1);
			treeStore(i+rowNum+1, rowNum+1);
		}
	}
	
	static int getShortest(){


		rowElements = (int) Math.pow(2, numRows-2);
		while(numRows>=1){

			for(int i = 1; i <= rowElements; i++){
				int first = treeList.get(treeList.size()-i);
				int second = treeList.get(treeList.size()-i-1);
				
				if(first < second){
					treeList.set(treeList.size()-i-1, second);
				}else{
					treeList.set(treeList.size()-i-1, first);
				}
				
				treeList.remove(treeList.size()-i);
			}

			for(int i = 1; i <= rowElements; i++){
				
				int firstAddLoc = treeList.size()-i-rowElements;
				int firstAdd = treeList.get(firstAddLoc);
				int lastItem = treeList.get(treeList.size()-i);
				
				treeList.set(firstAddLoc, firstAdd + lastItem);
			}

			for(int i = 1; i <= rowElements; i++){
				treeList.remove(treeList.size()-1);
			}
			
			numRows--;
			rowElements = (int) Math.pow(2, numRows-2);
		
		}
		
		return treeList.get(0);
		
	}
	
	static void inputNums(){
		
		 try{
			 
			 String[] temp;
		 
            FileReader fileReader = new FileReader(filename);

            BufferedReader bufferedReader = new BufferedReader(fileReader);

            while((line = bufferedReader.readLine()) != null) {
                
            	numRows++;
            	
                temp = line.split(" ");
                
                for(int i = 0; i < temp.length; i++){
                	triNums.add(Integer.parseInt(temp[i]));
                }
                
            }  

            bufferedReader.close();         
        }catch(FileNotFoundException ex) {
            System.out.println("Unable to open file '" + filename + "'");                
        }catch(IOException ex) {
            ex.printStackTrace();
        }
	}
	
}
