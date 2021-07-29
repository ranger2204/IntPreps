import java.util.Arrays;
import java.util.Stack;

class ValidParan {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        String open = "({[";
        String close = ")}]";
        for(char c: s.toCharArray()){
            System.out.println(String.format("%c", c));
            if(open.indexOf(c) != -1){
                stack.push(c);
            }
            else if(close.indexOf(c) != -1){
                int index = close.indexOf(c);
                char exp = open.charAt(index);
                
                char top = stack.pop();
                System.out.println(String.format("%c %c %c", c, exp, top));
                if(top != exp)
                    return false;
                
            }
        }
        return true;
        
    }

    public static void main(String[] args) {
        String s = "(]";
        ValidParan v = new ValidParan();
        v.isValid(s);
    }
}