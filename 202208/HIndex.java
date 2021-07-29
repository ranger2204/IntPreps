import java.util.Arrays;

class HIndex {
    
    public int computeIndex(int[] citations){
        Arrays.sort(citations);
        int hIndex = 0;
        for(int i=0;i<citations.length;i++){
            int v = citations[i];
            int d = citations.length - i;
            if(d >= v)
                hIndex = v;
            else{
                hIndex = Math.max(hIndex, d);
                break;
            }

        }
        return hIndex;
    }
}
