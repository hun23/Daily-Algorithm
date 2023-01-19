import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class n1018 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] inp = br.readLine().split(" ");
		int n = Integer.parseInt(inp[0]);
		int m = Integer.parseInt(inp[1]);
		ArrayList<char[]> board = new ArrayList<>();
		ArrayList<Integer> result = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			board.add(br.readLine().toCharArray());
		}
		for (int i = 0; i < n - 7; i++) {
			for (int j = 0; j < m - 7; j++) {
				int white = 0;
				int black = 0;
				for (int row = 0; row < 8; row++) {
					for (int col = 0; col < 8; col++) {
						if ((row + col) % 2 == 0) {
							if (board.get(i + row)[j + col] == 'W') {
								black += 1;
							} else {
								white += 1;
							}
						} else {
							if (board.get(i + row)[j + col] == 'W') {
								white += 1;
							} else {
								black += 1;
							}
						}
					}
				}
				result.add(Math.min(white, black));
			}
		}
		int mn = 2147483647;
		for (Integer i : result) {
			if (i < mn) {
					mn = i;
			}
		}
		bw.write(String.valueOf(mn) + "\n");
		bw.flush();
		bw.close();
	}
}