import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Stack;
import java.util.Arrays;

public class aaa {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] n_input = br.readLine().split(" ");
		int[] n_arr = new int[n];
		int m = Integer.parseInt(br.readLine());
		String[] m_input = br.readLine().split(" ");
		int[] m_arr = new int[m];

		for (int i = 0; i < n; i++) {
			n_arr[i] = Integer.parseInt(n_input[i]);
		}
		for (int i = 0; i < m; i++) {
			m_arr[i] = Integer.parseInt(m_input[i]);
		}

		Arrays.sort(n_arr);
		for (int m_num : m_arr) {
			int lo = 0;
			int hi = n_arr.length - 1;
			boolean found = false;
			if (n_arr[lo] == m_num || n_arr[hi] == m_num) {
				found = true;
			} else {
				while (lo + 1 < hi) {
					int mid = (lo + hi) / 2;
					if (m_num < n_arr[mid]) {
						hi = mid;
					} else if (n_arr[mid] < m_num) {
						lo = mid;
					} else {
						found = true;
						break;
					}
				}
			}
			if (found) {
				bw.write("1\n");
			} else {
				bw.write("0\n");
			}
		}
		bw.flush();
		bw.close();
	}
}