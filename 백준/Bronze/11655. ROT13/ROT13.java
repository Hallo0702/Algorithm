import java.io.*;
import java.sql.SQLOutput;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] word = br.readLine().split("");
        
        String answer = "";

        for (String s : word) {
            Character c = s.charAt(0);
            if (Character.isUpperCase(c)){
                Character chr = (char) (((int) c - (int) 'A' + 13) % 26 + (int) 'A');
                answer += chr;
            } else if (Character.isLowerCase(c)) {
                Character chr = (char) (((int) c - (int) 'a' + 13) % 26 + (int) 'a');
                answer += Character.toString(chr);
            } else {
                answer += s;
            }
        }

        System.out.println(answer);



    }
}
