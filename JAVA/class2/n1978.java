import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class n1978 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] inp = br.readLine().split(" ");
		int count = 0;
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(inp[i]);
			if (is_prime(num)) {
				count += 1;
			}
		}
		bw.write(String.valueOf(count) + "\n");
		bw.flush();
		bw.close();
	}

	public static boolean is_prime(int n) {
		if (n < 2) {
			return false;
		} else if (n <= 3) {
			return true;
		}
		int i = 2;
		while (i * i <= n) {
			if (n % i == 0) {
				return false;
			}
			i += 1;
		}
		return true;
	}
}