import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;

public class n11650 {
  public void run() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());
    HashMap<Integer, ArrayList> mp = new HashMap<>();
    
    for (int i=0; i<n; i++) {
      String[] st = br.readLine().split(" ");
      int x = Integer.parseInt(st[0]);
      int y = Integer.parseInt(st[1]);
      if (mp.get(x) == null) {
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(y);
        mp.put(x, arr);
      } else {
        mp.get(x).add(y);
      }
    }
    ArrayList<Integer> keys = new ArrayList<>(mp.keySet());
    Collections.sort(keys);
    for (Integer i : keys) {
      if (mp.get(i).size() == 1) {
        bw.write(String.valueOf(i) + " " + String.valueOf(mp.get(i).get(0)) + "\n");
      } else {
        ArrayList<Integer> sub = new ArrayList<>(mp.get(i));
        Collections.sort(sub);
        for (Integer j : sub) {
          bw.write(String.valueOf(i) + " " + String.valueOf(j) + "\n");
        }
      }
    }
    bw.flush();
    bw.close();
  }
}
