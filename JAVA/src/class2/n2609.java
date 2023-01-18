import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class aaa {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] inp = br.readLine().split(" ");
		int a = Integer.parseInt(inp[0]);
		int b = Integer.parseInt(inp[1]);

		// gcd = Greatest Common Divisor(최대공약수), LCM = lowest Common Multiple(최소공배수)
		int gcd = get_gcd(a, b);
		int lcm = a * b / gcd;
		bw.write(String.valueOf(gcd) + "\n");
		bw.write(String.valueOf(lcm) + "\n");
		bw.flush();
		bw.close();
	}

	// 유클리드 호제법
	public static int get_gcd(int a, int b) {
		while (true) {
			int r = a % b;
			if (r == 0) {
				return b;
			}
			a = b;
			b = r;
		}
	}
}