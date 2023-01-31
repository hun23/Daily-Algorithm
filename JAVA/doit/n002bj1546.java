import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n002bj1546 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] inp = br.readLine().split(" ");
		int sum = 0;
		int max = 0;
		for (String s : inp) {
			int num = Integer.parseInt(s);
			sum += num;
			max = Math.max(num, max);
		}
		bw.write(String.valueOf((double) sum / max / n * 100));
		bw.flush();
		bw.close();
	}
}