import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class n1259 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		while (true) {
			char[] inp = br.readLine().toCharArray();
			if (inp[0] == '0') {
				break;
			}
			int _len = inp.length;
			boolean p = true;
			for (int i = 0; i < _len/2; i++) {
				if (inp[i] != inp[_len - 1 - i]) {
					p = false;
					break;
				}
			}
			if (p) {
				bw.write("yes\n");
			} else {
				bw.write("no\n");
			}
		}

		bw.flush();
		bw.close();
	}
}