import java.util.Stack;

public class DecodeString {
    
    public static String decode(String encodedString){
        Stack<String> stk = new Stack<>();
        String curString = "";
        Integer curFreq = 0;
        for(int i=0;i<encodedString.length();i++){
            char c = encodedString.charAt(i);
            if(c == '['){
                stk.push(curString);
                stk.push(curFreq.toString());
                curString = "";
                curFreq = 0;

            }
            else if(c == ']'){
                int freq = Integer.parseInt(stk.pop());
                String popStr = stk.pop();
                curString = popStr + curString.repeat(freq);
                curFreq = 0;
            }
            else if(Character.isDigit(c)){
                curFreq = curFreq*10 + Character.getNumericValue(c);
            }
            else{
                curString += Character.toString(c);
            }

        }

        return curString;
    }


    public static void main(String[] args) {
        String[] tests = {
            "3[a]2[c]",
            "3[a2[c]]"
        };
        for(String t: tests){
            System.out.println(DecodeString.decode(t));
        }
    }
}
