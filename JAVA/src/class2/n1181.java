import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
	
public class n1181 {
	public static void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] inp = new String[n];
		ArrayList<String>[] arr = new ArrayList[50];
		for (int i = 0; i < 50; i++) {
			arr[i] = new ArrayList<String>();
		}
		for (int i = 0; i < n; i++) {
			inp[i] = br.readLine();
			arr[inp[i].length() - 1].add(inp[i]);
		}
		for (ArrayList<String> ss : arr) {
			Collections.sort(ss);
			String temp = "";
			for (String s : ss) {
				if (!temp.equals(s)) {
					bw.write(s + "\n");
				}
				temp = s;
			}
		}
		bw.flush();
		bw.close();
	}
}
