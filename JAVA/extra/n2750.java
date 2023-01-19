import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.io.IOException;

public class n2750 {
  public void run() throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    String s = br.readLine();
    int T = Integer.parseInt(s);
    int[] arr = new int[T];
    for (int i=0; i < T; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }
    Arrays.sort(arr);
    for (int i=0; i < T; i++) {
      bw.write(arr[i] + "\n");
    }
    bw.flush();
    bw.close();
  }
}
