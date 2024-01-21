import java.util.*;

class Challenge2{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        //To convert input to lowercase and to remove other non-alphabetic characters
        s=s.toLowerCase().replaceAll("[^a-zA-Z]","");
        System.out.println(longestPalindrome(s));
    }
    // Variables to store the result indices of the longest palindrome
    static int resultStart;
    static int resultLength;
    // Function to find the longest palindrome substring
    public static String longestPalindrome(String s){
         // If the length of the string is less than 2, it's already a palindrome
        if(s.length()<2){
            return s;
        }
        // Iterate through each character
        for(int i=0;i<s.length();i++){
            //for odd length palindromes
            expandRange(s,i,i);
            //for even length palindromes
            expandRange(s, i, i+1);
        }
        // Return the longest palindrome substring
        return s.substring(resultStart,resultStart+resultLength);
    }
    // Function to expand the palindrome range outward from the given indices
    public static void expandRange(String s,int begin,int end){
        while(begin>=0 && end<s.length() && s.charAt(begin)==s.charAt(end)){
            begin--;
            end++;
        }
        // If a longer palindrome is found during expansion, update result indices
        if(resultLength<end-begin-1){
            resultStart=begin+1;
            resultLength=end-begin-1;
        }
    }
}


/*
Test Case 1:
Input: "babad"
Output: "bab"

Test Case 2:
Input: "racecar"
Output: "racecar"

Test Case 3:
Input: "geeks12s23keeg"
Output: "geeksskeeg"

Test Case 4:
Input: "abcddcba"
Output: "abcddcba"

*/