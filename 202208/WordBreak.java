
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

public class WordBreak {

    public static boolean recurCheck(String word, int index, List<String> wordDict, HashMap<Integer, Boolean> memo, ArrayList<String> dictIndices){
        if(index >= word.length())
            return true;
        else{
            String sliced = word.substring(index, word.length());
            for(String d: wordDict){
                if(sliced.startsWith(d) && recurCheck(word, index+d.length(), wordDict, memo, dictIndices)){
                    dictIndices.add(d);
                    return true;
                }
            }
            return false;
        }
    }

    public static boolean checkWord(String word, List<String> wordDict){
        HashMap<Integer, Boolean> memo = new HashMap<>();
        ArrayList<String> stringIndices = new ArrayList<>();
        boolean ret = WordBreak.recurCheck(word, 0, wordDict, memo, stringIndices);
        System.out.println(ret);
        Collections.reverse(stringIndices);
        System.out.println(stringIndices);
        return ret;
    }

    // class Solution {
    //     public boolean wordBreak(String s, List<String> wordDict) {
            
    //     }
    // }


    public static void main(String[] args) {
        WordBreak.checkWord("carsandog", new ArrayList<String>(Arrays.asList("cars", "sand", "dog")));
        WordBreak.checkWord("cars", new ArrayList<String>(Arrays.asList("car", "ca", "rs")));
    }
}
