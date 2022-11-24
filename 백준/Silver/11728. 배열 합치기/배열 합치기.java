import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] A = new int[n];
        int[] B = new int[m];


        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < m; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }


        int x = 0;
        int y = 0;

        int[] answer = new int[n+m];

        while (x < n && y < m) {
            if (A[x] >= B[y]) {
                answer[x + y] = B[y];
                y++;
            } else {
                answer[x+y] = A[x];
                x++;
            }
        }

        if (x == n) {
            while (y < m) {
                answer[x+y] = B[y];
                y++;
            }
        } else if (y == m) {
            while (x < n) {
                answer[x+y] = A[x];
                x++;
            }
        }
        

        for (int i=0; i < n + m; i++) {
            bw.write(answer[i]+" ");
        }

        bw.flush();
        bw.close();


    }
}
