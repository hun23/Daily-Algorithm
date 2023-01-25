import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class n2751 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		// t개 수 입력받을 배열 생성 & 입력
		int[] arr = new int[t];
		for (int i = 0; i < t; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		// 정렬 및 출력
		Arrays.sort(arr);
		for (int num : arr) {
			bw.write(String.valueOf(num) + "\n");
		}
		bw.flush();
		bw.close();
	}
}