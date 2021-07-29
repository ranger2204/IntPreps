public class Permute {
    
    public void generate(String start, int index){
        if(index >= start.length()){
            System.out.println(start);
        }
        else{
            char[] chars = start.toCharArray();
            for(int i=index; i<start.length(); i++){
                if(index != i && start.charAt(index) == start.charAt(i))
                    continue;
                char tmp = chars[i];
                chars[i] = chars[index];
                chars[index] = tmp;
                this.generate(new String(chars), index+1);
            }
        }
    }

    public static void main(String[] args) {
        
        String[] tests = {
            "AXM", "AAA", "X"
        };
        for (String string : tests) {
            new Permute().generate(string, 0);
        }
    }

}
