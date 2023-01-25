import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class n10773 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// k 입력
		int k = Integer.parseInt(br.readLine());
		// 스택 생성
		Stack<Integer> stack = new Stack<>();
		int answer = 0;
		for (int i = 0; i < k; i++) {
			int num = Integer.parseInt(br.readLine());
			if (num != 0) {
				// 0이 아니면 answer에 더하고 stack에 push
				answer += num;
				stack.push(num);
			} else {
				// 0이면 stack 맨 위 값을 pop 후 answer 에서 빼기
				answer -= stack.pop();
			}
		}
		bw.write(String.valueOf(answer) + "\n");
		bw.flush();
		bw.close();
	}
}