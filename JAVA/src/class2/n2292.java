import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Queue;
import java.util.LinkedList;

public class aaa {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int plus = 1;
		int circle = 0;
		while (1 + 6 * circle < n) {
			circle += plus;
			plus += 1;
		}
		bw.write(String.valueOf(plus) + "\n");
		bw.flush();
		bw.close();
	}
}