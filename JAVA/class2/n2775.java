import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n2775 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// t입력 및 15 * 14 배열 생성
		int t = Integer.parseInt(br.readLine());
		int[][] aprt = new int[15][14];
		// 배열 초기화 및 초기값(0층) 입력
		for (int row = 0; row < 15; row++) {
			for (int col = 0; col < 14; col++) {
				if (row == 0) {
					aprt[row][col] = col + 1;
				} else {
					aprt[row][col] = 0;
				}
			}
		}
		// k, n 입력
		for (int i = 0; i < t; i++) {
			int k = Integer.parseInt(br.readLine());
			int n = Integer.parseInt(br.readLine());
			// 계산
			int answer = how_many(aprt, k, n - 1); // n-1을 입력해서 1호를 인덱스 0으로
			bw.write(String.valueOf(answer) + "\n");
		}
		// 배열 확인
		// for (int row = 0; row < 15; row++) {
		// for (int col = 0; col < 14; col++) {
		// bw.write(aprt[row][col] + " ");
		// }
		// bw.write("\n");
		// }
		bw.flush();
		bw.close();
	}

	private static int how_many(int[][] aprt, int k, int n) {
		int ret = 0;
		// 이미 값이 있으면
		if (aprt[k][n] != 0) {
			return aprt[k][n];
		}
		// k-1층 index 0 ~ index n까지 순회하며 더하기
		for (int i = 0; i <= n; i++) {
			ret += how_many(aprt, k - 1, i);
		}
		// 값 저장
		aprt[k][n] = ret;
		return ret;
	}
}