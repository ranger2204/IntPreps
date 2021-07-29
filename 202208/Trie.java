import java.util.HashMap;

class Node{
    public char c;
    public HashMap<Character, Node> links;
    public boolean isEndNode;

    public Node(char c){
        this.c = c;
        this.links = new HashMap<>();
        this.isEndNode = false;
    }

}
class Trie {
    private Node root;


    public Trie() {
        root = new Node(' ');
    }
    
    public void insert(String word) {
        Node cur = root;
        for(char c: word.toCharArray()){
            if(cur.links.containsKey(c)){
                cur = cur.links.get(c);
            }
            else{
                Node newNode = new Node(c);
                cur.links.put(c, newNode);
                cur = newNode;
            }
        }
        cur.isEndNode = true;
    }
    
    public boolean search(String word) {
        Node cur = root;
        for(char c: word.toCharArray()){
            if(cur.links.containsKey(c)){
                cur = cur.links.get(c);
            }
            else{
                return false;
            }
        }
        return cur.isEndNode;
    }
    
    public boolean startsWith(String prefix) {
        Node cur = root;
        for(char c: prefix.toCharArray()){
            if(cur.links.containsKey(c)){
                cur = cur.links.get(c);
            }
            else
                return false;
        }
        return true;
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */