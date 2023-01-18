import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class aaa {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// test case 수 입력
		int t = Integer.parseInt(br.readLine());
		for (int i = 0; i < t; i++) {
			// h w n 입력
			String[] inp = br.readLine().split(" ");
			int h = Integer.parseInt(inp[0]);
			int w = Integer.parseInt(inp[1]);
			int n = Integer.parseInt(inp[2]);
			// 몫(quo) 나머지(rem)
			int quo = (int) n / h;
			int rem = n % h;
			// 나머지가 0인경우 따로
			if (rem == 0) {
				rem = h;
			} else {
				quo += 1;
			}
			bw.write(String.valueOf(rem * 100 + quo) + "\n");
		}
		bw.flush();
		bw.close();
	}
}