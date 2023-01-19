import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class n2587 {
  public void run() throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int[] arr = new int[5];
    int sum = 0;
    for (int i=0; i < 5; i++) {
      int n = Integer.parseInt(br.readLine());
      arr[i] = n;
      sum += n;
    }
    sum /= 5;
    Arrays.sort(arr);
    bw.write(sum + "\n");
    bw.write(arr[2] + "\n");
    bw.flush();
    bw.close();
  }
}
