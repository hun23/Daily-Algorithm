import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class n1654 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] inp = br.readLine().split(" ");
		int k = Integer.parseInt(inp[0]);
		int n = Integer.parseInt(inp[1]);
		long[] arr = new long[k];
		long hi = 0;
		long lo = 1;
		for (int i = 0; i < k; i++) {
			int num = Integer.parseInt(br.readLine());
			arr[i] = num;
			if (num > hi) {
				hi = num;
			}
		}
		if (ok(arr, lo, n) == ok(arr, hi, n)) {
			bw.write(String.valueOf(hi) + "\n");
		} else {
			while (lo + 1 < hi) {
				long mid = (lo + hi) / 2;
				if (ok(arr, lo, n) == ok(arr, mid, n)) {
					lo = mid;
				} else if (ok(arr, mid, n) == ok(arr, hi, n)) {
					hi = mid;
				}
			}
			bw.write(String.valueOf(lo) + "\n");
		}
		bw.flush();
		bw.close();
	}

	public static boolean ok(long[] arr, long _len, int n) {
		int count = 0;
		for (long k : arr) {
			count += k / _len;
			if (count >= n) {
				return true;
			}
		}
		return false;
	}
}