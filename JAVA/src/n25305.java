import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class n25305 {
  public void run() throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    String[] inp = br.readLine().split(" ");
    String[] inpp = br.readLine().split(" ");
    int n = Integer.parseInt(inp[0]);
    int k = Integer.parseInt(inp[1]);
    int[] arr = new int[n];
    for (int i=0; i<n; i++) {
      arr[i] = Integer.parseInt(inpp[i]);
    }
    Arrays.sort(arr);
    bw.write(arr[n - k] + "\n");
    bw.flush();
    bw.close();
  }
}