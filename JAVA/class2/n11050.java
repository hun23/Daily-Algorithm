import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n11050 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// n, k 입력
		String[] inp = br.readLine().split(" ");
		int n = Integer.parseInt(inp[0]);
		int k = Integer.parseInt(inp[1]);
		int answer = 1;
		for (int i = n; i > 0; i--) {
			// n ~ k+1까지 곱하고 = n!/k!
			if (i > k) {
				answer *= i;
			}
			// n - k ~ 1까지 나누고 = ~/(n - k)!
			if ((n - k) >= i) {
				answer /= i;
			}
		}
		bw.write(String.valueOf(answer) + "\n");
		bw.flush();
		bw.close();
	}
}