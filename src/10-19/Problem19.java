import java.util.Calendar;

public class Problem19{
	
	public static void main(String []args){
		
		Calendar cal = Calendar.getInstance();
		
		int sundays = 0;
		int leap = 0;
		
		for(int i = 1901; i < 2001; i++){
			for(int j = 0; j < 12; j++){
				cal.set(i, j, 1);
				
				if(cal.get(Calendar.DAY_OF_WEEK) == 1 && cal.get(Calendar.DAY_OF_MONTH) == 1){
					sundays++;
				}
			}
		}
					
		System.out.println(sundays);
	}
}