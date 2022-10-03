import java.util.* ;
import java.io.*; 
public class Solution{
    public static int[][] pairSum(int[] arr, int s) {
        
        for (int i =0; i < arr.length; i++){
            for (int j = i + 1; j < arr.length; j++){
                if (arr[i] + arr[j] == s){
                    System.out.print(arr[i] + " " + arr[j]);
             
                }
                
                
            }
            
        } 
}
