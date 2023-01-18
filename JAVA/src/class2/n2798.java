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
		// n, m 입력
		String[] inp = br.readLine().split(" ");
		int n = Integer.parseInt(inp[0]);
		int m = Integer.parseInt(inp[1]);
		// n개 수 받을 배열 / used 배열 만들고 입력
		int[] arr = new int[n];
		boolean[] used = new boolean[n];
		String[] inp_nums = br.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(inp_nums[i]);
			used[i] = false;
		}
		// 재귀함수 시작
		int answer = choose(arr, used, 0, 0, m);

		bw.write(String.valueOf(answer) + "\n");
		bw.flush();
		bw.close();
	}

	public static int choose(int[] arr, boolean[] used, int depth, int sum, int m) {
		// 리턴값
		int ret = 0;
		// depth == 3이면(3장 뽑으면) 그때까지의 합계를 리턴
		if (depth == 3) {
			return sum;
		}
		for (int i = 0; i < arr.length; i++) {
			if (!used[i]) {
				used[i] = true;
				sum += arr[i];
				if (sum <= m) {
					// 리턴받은 값과 가지고 있던 값을 비교해서 큰 값을 저장
					ret = Math.max(ret, choose(arr, used, depth + 1, sum, m));
				}
				used[i] = false;
				sum -= arr[i];
			}
		}
		// 모든 경우의 수를 돌아본 뒤 가장 큰 값 리턴
		return ret;
	}
}