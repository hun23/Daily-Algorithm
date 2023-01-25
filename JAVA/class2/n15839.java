import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n15839 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// n 입력
		int n = Integer.parseInt(br.readLine());
		int p = 31;
		int m = 1234567891;
		// 입력 문장 숫자 배열로 변경
		char[] inp = br.readLine().toCharArray();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = inp[i] - 'a' + 1;
		}
		long answer = 0; // long 사용
		for (int j = 0; j < n; j++) {
			answer += multiply(arr[j], m, p, j);
			if (answer > m) { // answer이 m보다 커지면 나머지만 남김
				answer = answer % m;
			}
		}
		bw.write(String.valueOf(answer) + "\n");
		bw.flush();
		bw.close();
	}

	private static long multiply(int a, int m, int p, int idx) throws IOException {
		long ret = a;
		for (int i = 0; i < idx; i++) {
			ret = ret * p;
			if (ret > m) { // ret이 m보다 커지면 나머지만 남김
				ret = ret % m;
			}
		}
		return ret;
	}
}