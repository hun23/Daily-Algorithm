import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Stack;

public class n1874 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		ArrayList<Character> answer = new ArrayList<>();
		Stack<Integer> stack = new Stack<>();

		int ascending = 1;
		boolean no = false;
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(br.readLine());
			if (!no) {
				while (ascending <= num) {
					stack.push(ascending);
					answer.add('+');
					ascending += 1;
				}
				if (stack.peek() == num) {
					stack.pop();
					answer.add('-');
				} else {
					no = true;
				}
			}
		}
		if (no) {
			bw.write("NO\n");
		} else {
			for (char c : answer) {
				bw.write(c + "\n");
			}
		}
		bw.flush();
		bw.close();
	}
}