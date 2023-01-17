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
		String[] inp = br.readLine().split(" ");
		int m = Integer.parseInt(inp[0]);
		int n = Integer.parseInt(inp[1]);
		boolean[] is_prime_arr = new boolean[n + 1];
		Arrays.fill(is_prime_arr, true);
		is_prime_arr[0] = false;
		is_prime_arr[1] = false;
		int i = 2;
		while (i < n) {
			if (i * i > n) {
				break;
			}
			for (int j = i + i; j < n + 1; j+=i) {
				if (is_prime_arr[j]) {
					is_prime_arr[j] = false;
				}
			}
			i += 1;
		}
		int num = 0;
		for (boolean b : is_prime_arr) {
			if (b && num >= m) {
				bw.write(String.valueOf(num) + "\n");
			}
			num += 1;
		}
		bw.flush();
		bw.close();
	}
}