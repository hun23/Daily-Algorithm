import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n001bj11720 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		char[] inp = br.readLine().toCharArray();
		int sum = 0;
		for (char c : inp) {
			sum += (c - '0');
		}
		bw.write(String.valueOf(sum));
		bw.flush();
		bw.close();
	}
}