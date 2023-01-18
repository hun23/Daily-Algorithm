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
		// 입력
		int t = Integer.parseInt(br.readLine());
		// t번 반복
		for (int i = 0; i < t; i++) {
			char[] inp = br.readLine().toCharArray();
			int count = 0;
			// 짝이 맞으면 yes = true
			boolean yes = true;
			for (char c : inp) {
				if (c == '(') {
					count += 1;
				} else {
					count -= 1;
				}
				// count < 0 => ')'가 더 많다
				if (count < 0) {
					yes = false;
					break;
				}
			}
			// count > 0 => '('가 더 많다
			if (count > 0) {
				yes = false;
			}
			if (yes) {
				bw.write("YES\n");
			} else {
				bw.write("NO\n");
			}
			bw.flush();
		}
		bw.close();
	}
}