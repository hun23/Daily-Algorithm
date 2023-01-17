import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class n1436 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int i = 0;
		int count = 0;
		while (true) {
			i += 1;
			if (doom(i)) {
				count += 1;
				if (count == n) {
					bw.write(String.valueOf(i) + "\n");
					break;
				}
			}
		}
		bw.flush();
		bw.close();
	}

	public static boolean doom(int i) {
		char[] c_arr = String.valueOf(i).toCharArray();
		int doom_count = 0;
		for (char c : c_arr) {
			if (c == '6') {
				doom_count += 1;
			} else {
				doom_count = 0;
			}
			if (doom_count == 3) {
				return true;
			}
		}
		return false;
	}
}