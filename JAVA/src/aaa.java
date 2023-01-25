import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.io.File;
import java.io.FileReader;

public class aaa {
	public void run() throws IOException {
		File note = new File("C:\\Users\\SSAFY\\Desktop\\ssafy\\Daily-Algorithm\\TESTCASE\\2805.txt");
		BufferedReader br = new BufferedReader(new FileReader(note));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// // n, m 입력
		String[] inp = br.readLine().split(" ");
		int n = Integer.parseInt(inp[0]);
		int m = Integer.parseInt(inp[1]);
		// // arr 입력
		String[] arr_inp = br.readLine().split(" ");
		int[] arr = new int[n];
		int mx = 0;
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(arr_inp[i]);
			arr[i] = num;
			if (num > mx) {
				mx = num;
			}
		}
		// 이분탐색 초기값 설정
		int lo = 0;
		int hi = mx;
		int mid;
		int j = -1;
		// 이분탐색 시작
		while (lo + 1 < hi) {
			mid = (hi + lo) / 2;
			bw.write(String.valueOf(++j) + ": " + String.valueOf(mid) + "\n");
			if (check(arr, m, mid)) {
				lo = mid;
			} else {
				hi = mid;
			}
		}
		bw.write(String.valueOf(lo) + "\n");
		bw.flush();
		bw.close();
		br.close();
	}

	private static boolean check(int[] arr, int m, int mid) {
		// int _sum = 0; 오버플로우 조심!
		long _sum = 0;
		for (int a : arr) {
			if (a > mid) {
				_sum += (a - mid);
			}
			if (_sum >= m) {
				return true;
			}
		}
		return false;
	}
}