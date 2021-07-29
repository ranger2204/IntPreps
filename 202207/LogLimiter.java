import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.HashMap;

class LogLimiter{

    HashMap<String, Integer> lookup;
    int window;

    LogLimiter(int timeWindow){
        lookup = new HashMap<>();
        window = timeWindow;
    }

    public boolean printMsg(String msg, Integer timestamp){
        if(lookup.containsKey(msg)){
            int lastTime = lookup.get(msg);
            if(timestamp - lastTime >= window){
                lookup.put(msg, timestamp);
                return true;
            }
            return false;
        }
        else{
            lookup.put(msg, timestamp);
            return true;
        }
    }

    public static void main(String[] args){
        List<String> msgs = Arrays.asList("foo", "bar", "foo", "foo", "bar");
        List<Integer> timestamps = Arrays.asList(1, 2, 3, 4, 5);
        LogLimiter logger = new LogLimiter(2);
        for(int i=0;i<msgs.size();i++){
            System.out.println(logger.printMsg(msgs.get(i), timestamps.get(i)));
        }

    }
}