import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class n2869 {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// a, b, v 입력
		String[] inp = br.readLine().split(" ");
		int a = Integer.parseInt(inp[0]);
		int b = Integer.parseInt(inp[1]);
		int v = Integer.parseInt(inp[2]);
		// 하루에
		int daily = a - b;
		// 마지막날 전까지 올라가야 하는 높이
		int before_last_day = v - a;
		// 마지막날 전까지 올라가야 하는 높이 이상으로 도달하는데 필요한 일수
		int quo = before_last_day / daily;
		int rem = before_last_day % daily;
		// = 몫 or 몫 + 1 (나머지가 있는 경우)
		int days = quo + (rem != 0 ? 1 : 0);
		bw.write(String.valueOf(days + 1) + "\n");
		bw.flush();
		bw.close();
	}
}