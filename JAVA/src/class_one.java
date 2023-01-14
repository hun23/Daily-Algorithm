import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class class_one {
	public void n1001() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);
        bw.write(String.valueOf(a - b) + "\n");
        bw.flush();
        bw.close();
	}

    public void n1008() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);
        double re = (double) a/b;
        bw.write(String.valueOf(re) + "\n");
        bw.flush();
        bw.close();
    }
	
    public void n1152() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().trim().split(" ");
        int re = arr.length;
        if (re == 1 && arr[0].isEmpty()) {
            bw.write("0\n");
        } else {
            bw.write(String.valueOf(re) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public void n1330() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);
        if (a > b) {
            bw.write(">\n");
        } else if (a < b) {
            bw.write("<\n");
        } else {
            bw.write("==\n");
        }
        bw.flush();
        bw.close();
    }

    public void n1157() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[] arr = br.readLine().toCharArray();
        int[] counts = new int[256];
        for (char c : arr) {
            if ('z' >= c && c >= 'a') {
                c += ('A' - 'a');
            }
            counts[(int)c] += 1;
        }
        int mx = 0;
        int re = 0;
        int idx = 0;
        for (int count : counts) {
            if (count > mx) {
                mx = count;
                re = idx;
            } else if (count == mx) {
                re = -1;
            }
            idx += 1;
        }
        if (re == -1) {
            bw.write("?\n");
        } else {
            if ('z' >= re && re >= 'a') {
                re += ('A' - 'a');
            }
            bw.write(((char)re) + "\n");
        }
        bw.flush();
        bw.close();
    }
}
