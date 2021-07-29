class ValidateNumber{
    public static final boolean validaNumericString(String numStr){
        int expCount = 1;
        int decCount = 1;
        int sign_count = 1;
        for(int i=0;i<numStr.length();i++){
            char c = numStr.charAt(i);
            if(Character.isDigit(c))
                continue;
            else if( c == '+' || c == '-'){
                if( i == 0 & sign_count > 0)
                    sign_count -= 1;
                else
                    return false;
            }
            else if(c == '.' & i != 0){
                if(decCount > 0){
                    decCount -= 1;
                }
                else
                    return false;
            }
            else if( c == 'e' & i != 0){
                if(expCount > 0)
                    expCount -= 1;
                else
                    return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String[] tests = {
            "10.1",
            "-10.1",
            "1e5",
            "1.025e10",
            "1e10.25"
        };

        for(String t: tests){
            System.out.println(String.format("%s %b", t, ValidateNumber.validaNumericString(t)));
        }
    }
}