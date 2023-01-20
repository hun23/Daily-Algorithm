import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Collections;

public class n10989 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// n입력, 배열 및 해쉬맵 생성
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> arr = new ArrayList<>();
		HashMap<Integer, Integer> map = new HashMap<>();
		// 숫자 입력
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(br.readLine());
			// 값이 없으면
			if (map.get(num) == null) {
				map.put(num, 1);
				arr.add(num);
				// 이미 있으면 +1
			} else {
				map.put(num, map.get(num) + 1);
			}
		}
		// arr 정렬
		Collections.sort(arr);
		for (int num : arr) { // arr를 순회하면서
			for (int k = 0; k < map.get(num); k++) { // map에 적힌 순서만큼
				bw.write(String.valueOf(num) + "\n"); // 출력
			}
		}
		bw.flush();
		bw.close();
	}
}