import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class n1966 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int[] answer = new int[t];
		int ans_count = 0;
		for (int i = 0; i < t; i++) {
			String[] nm = br.readLine().split(" ");
			int n = Integer.parseInt(nm[0]);
			int m = Integer.parseInt(nm[1]);
			ArrayList<Integer> importance = new ArrayList<>();
			ArrayList<Boolean> target = new ArrayList<>();
			String[] inp = br.readLine().split(" ");
			for (int j = 0; j < n; j++) {
				importance.add(Integer.parseInt(inp[j]));
				if (j != m) {
					target.add(false);
				} else {
					target.add(true);
				}
			}
			int mx = 0;
			int count = 1;
			while (true) {
				mx = get_max(importance);
				if (importance.get(0) == mx) {
					if (target.get(0)) {
						answer[ans_count] = count;
						ans_count += 1;
						break;
					}
					importance.remove(0);
					target.remove(0);
					count += 1;
				} else {
					int temp = importance.get(0);
					boolean btemp = target.get(0);
					importance.remove(0);
					target.remove(0);
					importance.add(temp);
					target.add(btemp);
				}
			}
			answer[i] = count;
		}
		for (int a : answer) {
			bw.write(String.valueOf(a) + "\n");
		}
		bw.flush();
		bw.close();
	}

	public static int get_max(ArrayList<Integer> arr) {
		int mx = 0;
		for (int i : arr) {
			mx = Math.max(i, mx);
		}
		return mx;
	}
}