public class NextPerm {
    public static String compute(String baseString){
        char[] chars = baseString.toCharArray();
        int pivot = -1;
        int strLen = baseString.length();
        for(int i=0;i<strLen;i++){
            if(i==0)
                continue;
            else{
                int j = strLen - i -1;
                int a = Character.getNumericValue(chars[j]);
                int b = Character.getNumericValue(chars[j+1]);
      
                if(a < b){
                    pivot = j;
                    break;
                }
            }
        }

        if(pivot  == -1){
            return "Pivot -1";
        }
        else{
            float maxDiff = Float.POSITIVE_INFINITY;
            int minSI = -1;
            for(int i=pivot+1; i<strLen; i++){
                int a = Character.getNumericValue(chars[pivot]);
                int b = Character.getNumericValue(chars[i]);
                int d = b - a;
                if(d > 0 && d < maxDiff){
                    minSI = i;
                    maxDiff = d;
                }
            }
            if(minSI != -1){
                char t = chars[minSI];
                chars[minSI] = chars[pivot];
                chars[pivot] = t;
                return new String(chars);
            }
            return "";
        }
    }

    public static void main(String[] args) {
        String[] tests = {
            "123",
            "48900"

        };
        for (String t : tests) {
            System.out.println(NextPerm.compute(t));
        }
    }
}
