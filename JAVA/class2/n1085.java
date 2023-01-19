import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n1085 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] inp = br.readLine().split(" ");
		int x = Integer.parseInt(inp[0]);
		int y = Integer.parseInt(inp[1]);
		int w = Integer.parseInt(inp[2]);
		int h = Integer.parseInt(inp[3]);
		int xmin = Math.min(x, w - x);
		int ymin = Math.min(y, h - y);
		bw.write(String.valueOf(Math.min(xmin, ymin)) + "\n");
		bw.flush();
		bw.close();
	}
}