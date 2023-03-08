import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n003bj11659 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] inp = br.readLine().split(" ");
		int n = Integer.parseInt(inp[0]);
		int m = Integer.parseInt(inp[1]);
		String[] inp2 = br.readLine().split(" ");
		int[] arr = new int[n];
		int[] part_sum = new int[n]; // 부분합배열
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(inp2[i]);
			arr[i] = num;
			if (i != 0) {
				part_sum[i] = part_sum[i - 1] + num;
			} else {
				part_sum[i] = num;
			}
		}
		for (int j = 0; j < m; j++) {
			String[] inp3 = br.readLine().split(" ");
			int a = Integer.parseInt(inp3[0]);
			int b = Integer.parseInt(inp3[1]);
			int answer;
			if (a == 1) {
				answer = part_sum[b - 1];
			} else {
				answer = part_sum[b - 1] - part_sum[a - 1 - 1];
			}
			bw.write(String.valueOf(answer) + "\n");
		}
		bw.flush();
		bw.close();
	}
}