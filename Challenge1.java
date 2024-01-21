import java.util.*;

class Challenge1{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        ArrayList<Integer> input=new ArrayList<>();
        //Takes input until a non-integer is entered
        while(sc.hasNextInt()){
            input.add(sc.nextInt());
        }
        //function to apply kadane's algorithm to find the maximum sum subarray
        int result=max_subarray_sum(input);
        //To display the result
        System.out.println(result);
        //scanner close
        sc.close();
    }
    public static int max_subarray_sum(ArrayList<Integer> input){
        int sum=0;
        int max=Integer.MIN_VALUE;
        //Iterate through the array
        for(int num: input){
            //Adds array element to sum
            sum=sum+num;
            //Update the maximum sum
            max=Math.max(sum,max);
            if(sum<0){
                sum=0;
            }
        }
        //return the maximum sum
        return max;
    }
}
/* 
Test Case-1:
Input: 1 -2 3 4 -1 2 -3 5 -4 
Output: 10 

Test Case-2:
Input: 5 4 -1 7 8
Output: 23

Test Case-3:
Input: -2 1 -3 4 -1 2 1 -5 4
Output: 6

Test Case-4:
Input: 1
Output: 1
*/ 