import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Collections;

public class n2108 {
  public void run() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());
    int sum = 0;
    int[] arr = new int[n];
    HashMap<Integer, Integer> mp = new HashMap<>(8001);
    for (int i=0; i<n; i++) {
      int num = Integer.parseInt(br.readLine());
      sum += num;
      arr[i] = num;
      if (mp.get(num) == null) {
        mp.put(num, 1);
      } else {
        mp.put(num, mp.get(num) + 1);
      }
    }
    Arrays.sort(arr);

    int mx = -2147483648;
    ArrayList<Integer> keys = new ArrayList<>();
    for (Integer i : mp.keySet()) {
      if (mp.get(i) > mx) {
        mx = mp.get(i);
        keys.clear();
        keys.add(i);
      } else if (mp.get(i) == mx) {
        keys.add(i);
      }
    }
    double avg = (double)sum / n;
    Collections.sort(keys);

    // bw.write(String.format("%.0f", avg) + "\n");
    bw.write(String.valueOf(Math.round(avg)) + "\n");
    bw.write(String.valueOf(arr[Math.round((n - 1) / 2)] + "\n"));
    // 최빈값
    if (keys.size() != 1) {
      bw.write(String.valueOf(keys.get(1)) + "\n");
    } else {
      bw.write(String.valueOf(keys.get(0)) + "\n");
    }
    bw.write(arr[n - 1] - arr[0] + "\n");
    bw.flush();
    bw.close();
  }
}
