import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n4153 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// 입력
		while (true) {
			String[] inp = br.readLine().split(" ");
			int a = Integer.parseInt(inp[0]);
			int b = Integer.parseInt(inp[1]);
			int c = Integer.parseInt(inp[2]);
			if (a + b + c == 0) {
				break;
			}
			if (is_jikgak(a, b, c)) {
				bw.write("right\n");
			} else {
				bw.write("wrong\n");
			}
		}
		bw.flush();
		bw.close();
	}

	public static boolean is_jikgak(int a, int b, int c) {
		int mx = 0;
		if (a >= b) {
			mx = Math.max(a, c);
		} else {
			mx = Math.max(b, c);
		}
		int ab = 0;
		if (a - mx < 0) {
			ab += a * a;
		}
		if (b - mx < 0) {
			ab += b * b;
		}
		if (c - mx < 0) {
			ab += c * c;
		}
		if (ab == mx * mx) {
			return true;
		}
		return false;
	}
}