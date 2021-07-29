
import java.util.Arrays;

class SplitToPalindrome {
     public static String getLongestPalindrome(String s){
        int m = s.length();

        int[][] mat = new int[m][m];
        for(int i=0;i<m;i++){
            for(int j=0;j<m;j++)
                mat[i][j] = 0;
        }

        for(int i=0;i<m;i++){
            mat[i][i] = 1;
            if(i < m-1){
                if(s.charAt(i) == s.charAt(i+1))
                    mat[i][i+1] = 1;
            }
        }

        int longest = 0;
        String result = null;
        for(int j=1; j< m;j++){
            int r = j;
            for(int i=0;i<m-1;i++){
                if(r < m && (s.charAt(i) == s.charAt(r)) && mat[i+1][r-1] == 1){
                    mat[i][r] = 1;
                    if(r -i > longest){
                        longest = r - i;
                        result = s.substring(i, r+1);
                    }
                }
                r += 1;
            }
        }
        
        // for(int i=0; i<m;i++)
        //     System.out.println(Arrays.toString(mat[i]));
    
        // ArrayList<String> palindromes = new ArrayList<>();
        // return (String[])palindromes.toArray();
        return result;
     }
     public static void main(String[] args) {
         String[] strs = {"malayalam", "kayak", "racecarkayak"};

         for(String s: strs){
            System.out.println(SplitToPalindrome.getLongestPalindrome(s));
         }
         
     }
}