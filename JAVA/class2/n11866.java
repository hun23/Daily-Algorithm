import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class n11866 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// n, k 입력
		String[] inp = br.readLine().split(" ");
		int n = Integer.parseInt(inp[0]);
		int k = Integer.parseInt(inp[1]);
		// queue생성 및 답 저장 배열 생성
		Queue<Integer> que = new LinkedList<>();
		int[] answer = new int[n];
		for (int i = 1; i < n + 1; i++) {
			que.add(i);
		}
		int kill = 1;
		// 순회하며 제거
		while (!que.isEmpty()) {
			int temp = que.poll();
			if (kill % k == 0) {
				// answer에 인덱스가 필요하기 때문에
				// kill을 계속 쌓으며 몫을 인덱스로 사용
				answer[(int) (kill / k) - 1] = temp;
			} else {
				que.add(temp);
			}
			kill += 1;
		}
		// 답 출력 형식 위한 StringBuilder
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		for (int j = 0; j < n; j++) {
			if (j != n - 1) {
				sb.append(String.valueOf(answer[j])).append(", ");
			} else {
				sb.append(String.valueOf(answer[j]));
			}
		}
		bw.write(sb.toString() + ">\n");
		bw.flush();
		bw.close();
	}
}