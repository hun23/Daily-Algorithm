import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Collections;

public class n7568 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// n 입력
		int n = Integer.parseInt(br.readLine());
		// 덩치(int[2]) 입력할 ArrayList생성
		ArrayList<int[]> arr = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			// 덩치(int[2])를 ArrayList에 입력
			String[] inp = br.readLine().split(" ");
			int[] dungchi = new int[2];
			dungchi[0] = Integer.parseInt(inp[0]);
			dungchi[1] = Integer.parseInt(inp[1]);
			arr.add(dungchi);
		}
		for (int j = 0; j < n; j++) {
			int big_count = 1;
			for (int k = 0; k < n; k++) {
				// arr.get(k)가 arr.get(j)보다 크면
				if (is_first_big(arr.get(k), arr.get(j))) {
					big_count += 1;
				}
			}
			bw.write(String.valueOf(big_count) + ((j == n - 1) ? "" : " "));
		}
		bw.flush();
		bw.close();
		br.close();
	}

	private static boolean is_first_big(int[] a, int[] b) {
		if (a[0] > b[0] && a[1] > b[1]) {
			return true;
		}
		return false;
	}
}