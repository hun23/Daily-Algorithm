import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Queue;
import java.util.LinkedList;

public class n2164 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		Queue<Integer> arr = new LinkedList<>();
		for (int i = 0; i < n; i++) {
			arr.add(i + 1);
		}
		boolean discard = true;
		while (arr.size() != 1) {
			if (discard) {
				arr.remove();
			} else {
				arr.add(arr.poll());
			}
			discard = !discard;
		}
		bw.write(String.valueOf(arr.poll()) + "\n");
		bw.flush();
		bw.close();
	}
}