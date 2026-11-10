class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> bracket = new HashMap<>();
        bracket.put('}', '{');
        bracket.put(']', '[');
        bracket.put(')', '(');
        for(char c: s.toCharArray()){
            if(bracket.containsKey(c)){
                if(!stack.isEmpty() && stack.peek() == bracket.get(c)){
                    stack.pop();
                }else{
                    return false;
                }
            }else{
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
