import java.io.*;

//RECURSION WORKS FOR SMALL CASES

public class Problem81 {

	static int dim = 80;
	
	static int[][] matrix = new int[dim][dim];
	
	public static void main(String[] args) {

		storeMatrix();
		/*matrix[0][0] = 131;
		matrix[1][0] = 673;
		matrix[2][0] = 234;
		matrix[3][0] = 103;
		matrix[4][0] = 18;
		
		matrix[0][1] = 201;
		matrix[1][1] = 96;
		matrix[2][1] = 342;
		matrix[3][1] = 965;
		matrix[4][1] = 150;
		
		matrix[0][2] = 630;
		matrix[1][2] = 803;
		matrix[2][2] = 746;
		matrix[3][2] = 422;
		matrix[4][2] = 111;
		
		matrix[0][3] = 537;
		matrix[1][3] = 699;
		matrix[2][3] = 497;
		matrix[3][3] = 121;
		matrix[4][3] = 956;
		
		matrix[0][4] = 805;
		matrix[1][4] = 732;
		matrix[2][4] = 524;
		matrix[3][4] = 37;
		matrix[4][4] = 331;*/
		System.out.println(getShortest(dim-1, dim-1));
		
	}
	
	static int getShortest(int i, int j){
		if(i == 0){
			return getSum(0, j);
		}else if(j == 0){
			return getSum(i, 0);
		}else if(getShortest(i-1, j) < getShortest(i, j-1)){
			return getShortest(i-1, j) + matrix[i][j];
		}else{
			return getShortest(i, j-1) + matrix[i][j];
		}
		
	}
	
	static int getSum(int i, int j){
		
		int out = 0;
		
		if(i == 0){
			for(int k = 0; k <= j; k++){
				out+=matrix[i][k];
			}
		}
		
		if(j == 0){
			for(int k = 0; k <= i; k++){
				out+=matrix[k][j];
			}
		}
		
		return out;
		
	}
	
	static void storeMatrix(){
		String fileName = "p081_matrix.txt";
		
        String line = null;

        try {
            FileReader fileReader =  new FileReader(fileName);

            BufferedReader bufferedReader = new BufferedReader(fileReader);

            for(int i = 0; i<80; i++){
	            while((line = bufferedReader.readLine()) != null) {
	            	String[] parts = line.split(",");
	                for(int j = 0; j < parts.length; j++){
	                	matrix[i][j] = Integer.parseInt(parts[j]);
	                }
	            }   
            }

            bufferedReader.close();         
        }
        catch(FileNotFoundException ex) {
            System.out.println("Unable to open file '" + fileName + "'");                
        }
        catch(IOException ex) {
            System.out.println("Error reading file '" + fileName + "'");     
        }
		
	}

}
