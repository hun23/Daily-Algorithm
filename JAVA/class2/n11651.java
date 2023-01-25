import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Collections;

public class n11651 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// n 입력
		int n = Integer.parseInt(br.readLine());
		// y길이를 key, int를 담을 ArrayList를 value값으로 하는hashmap 생성
		HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
		// arr 입력
		for (int i = 0; i < n; i++) {
			String[] inp = br.readLine().split(" ");
			int x = Integer.parseInt(inp[0]);
			int y = Integer.parseInt(inp[1]);
			if (map.containsKey(y)) {
				map.get(y).add(x);
			} else {
				ArrayList<Integer> new_list = new ArrayList<>();
				new_list.add(x);
				map.put(y, new_list);
			}
		}
		// hashmap key값 정렬
		ArrayList<Integer> sorted_key_list = new ArrayList<>(map.keySet());
		Collections.sort(sorted_key_list);
		for (Integer key : sorted_key_list) { // 정렬된 key값 순서로
			Collections.sort(map.get(key)); // 내부 리스트 정렬 후
			for (Integer x : map.get(key)) { // 고대로 출력
				bw.write(String.valueOf(x) + " " + String.valueOf(key) + "\n");
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}