import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Collections;
import java.util.Arrays;

public class aaa {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// n 입력, n_arr 입력 및 이분탐색 위한 정렬
		int n = Integer.parseInt(br.readLine());
		int[] n_arr = new int[n];
		String[] n_inp = br.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			n_arr[i] = Integer.parseInt(n_inp[i]);
		}
		Arrays.sort(n_arr);
		// 같은 방식으로 m 입력, m_arr 입력
		int m = Integer.parseInt(br.readLine());
		int[] m_arr = new int[n];
		String[] m_inp = br.readLine().split(" ");
		for (int j = 0; j < m; j++) {
			m_arr[j] = Integer.parseInt(m_inp[j]);
		}
		// hashmap 생성
		HashMap<Integer, Integer> map = new HashMap<>();
		// m_arr 순회하며 hashmap에 추가
		for (int k = 0; k < m; k++) {
			int count = 0;
			if (map.containsKey(m_arr[k])) {
				count = map.get(m_arr[k]);
			} else {
				count = map.put(m_arr[k], count(n_arr, m));
			}
			bw.write(String.valueOf(count) + ((k == m - 1) ? "" : " "));
		}
		bw.flush();
		bw.close();
		br.close();
	}

	private static boolean check(int[] n_arr, int idx, int m) {
		if (n_arr[idx] >= m) {
			return true;
		}
		return false;
	}

	private static int find_range(int[] n_arr, int idx) {
		// idx 위로 같은 값 찾기
		int i = 0;
		int start = 0;
		int end = 0;
		while (idx + 1 != n_arr.length && n_arr[idx] != n_arr[idx + i]) {
			end = idx + i;
		}
		i = 0;
		while (idx >= 0 && n_arr[idx] != n_arr[idx - i]) {
			start = idx - i;
		}
		return (end - start + 1);
	}

	private static int count(int[] n_arr, int m) {
		int _len = n_arr.length;
		// 이분탐색 초기설정
		int lo = 0;
		int hi = _len - 1;
		// 찾는 값이 양 끝에 있는 경우
		boolean lo_checked = check(n_arr, lo, m);
		if (lo_checked == check(n_arr, hi, m)) {
			if (lo_checked) {
				find_range(n_arr, 0);
			} else {
				find_range(n_arr, n_arr.length - 1);
			}
		}
		// 이분탐색
		while (lo + 1 < hi) {
			int mid = (lo + hi) / 2;
			lo_checked = check(n_arr, lo, m);
			boolean mid_checked = check(n_arr, mid, m);
			if (lo_checked != mid_checked) {
				hi = mid;
			} else {
				lo = mid;
			}
		}
		return find_range(n_arr, lo);
	}
}