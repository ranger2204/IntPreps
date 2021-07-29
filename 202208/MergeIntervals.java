import java.util.Arrays;
import java.util.Comparator;

public class MergeIntervals {
    
    public static int[][] merge(int[][] intervals){
        int m = intervals.length;
        int[][] result = new int[m][2];

        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));
        result[0] = intervals[0].clone();
        int arrIndex = 0;
        for(int i=1; i<m;i++){
            if(result[arrIndex][1] >= intervals[i][0]){
                result[arrIndex][1] = Math.max(intervals[i][1], result[arrIndex][1]);
            }
            else{
                arrIndex += 1;
                result[arrIndex] = intervals[i].clone();
            }
        }

        
        return Arrays.copyOfRange(result, 0, arrIndex+1);
    }

    public static void main(String[] args) {
        int[][] intervals = {
            {1, 4},
            {4, 5},
            {6, 7},
            {8, 10},
            {9, 10}
        };

        int[][] result = MergeIntervals.merge(intervals);

        for(int i=0;i<result.length;i++)
            System.out.println(Arrays.toString(result[i]));

    }
}
