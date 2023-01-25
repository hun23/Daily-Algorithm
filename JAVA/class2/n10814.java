import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class n10814 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// test case 수 입력
		int t = Integer.parseInt(br.readLine());
		// 인덱스가 나이 - 1인 배열 생성 및 초기화
		ArrayList<String>[] ages = new ArrayList[200];
		for (int i = 0; i < 200; i++) {
			ages[i] = new ArrayList<String>();
		}
		for (int j = 0; j < t; j++) {
			// h w n 입력
			String[] inp = br.readLine().split(" ");
			int age = Integer.parseInt(inp[0]);
			String name = inp[1];
			// 나이에 맞는 배열에 추가
			ages[age - 1].add(name);
		}
		// 순회하며 출력
		for (int k = 0; k < 200; k++) {
			for (String n : ages[k]) {
				bw.write(String.valueOf(k + 1) + " " + n + "\n");
			}
		}
		bw.flush();
		bw.close();
	}
}