class Solution {

    StringBuilder sb = new StringBuilder();

    public String encode(List<String> strs) {

        for(String st: strs){
            sb.append(st.length()).append('#');
            sb.append(st);
        }
        return sb.toString();
    }

        public List<String> decode(String str) {
        char[] ch = str.toCharArray();
        StringBuilder s = new StringBuilder();
        ArrayList<String> words = new ArrayList<>();

        for (int i = 0; i < ch.length; i++) {
            if (ch[i] == '#') {
                int num = Integer.parseInt(s.toString());
                s.setLength(0);
                i++; // move past '#'

                for (int j = 0; j < num; j++) {
                    s.append(ch[i + j]);
                }

                words.add(s.toString());
                s.setLength(0);
                i += num - 1; // minus 1 because outer loop will also increment i
            } else {
                s.append(ch[i]);
            }
        }

        return words;
    }

}
