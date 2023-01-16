import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.nio.Buffer;

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

    public void n1546() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");
        int mx = 0;
        int sum = 0;
        for (String s : arr) {
            int num = Integer.parseInt(s);
            mx = Math.max(mx, num);
            sum += num;
        }
        double re = (double) sum / mx * 100 / arr.length;
        bw.write(String.valueOf(re) + "\n");
        bw.flush();
        bw.close();
    }

    public void n2438() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                bw.write("*");
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }

    public void n2439() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                bw.write(" ");
            }
            for (int j = 0; j < i + 1; j++) {
                bw.write("*");
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }

    public void n2475() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int sum = 0;
        int num = 0;
        for (int i = 0; i < 5; i++) {
            num = Integer.parseInt(arr[i]);
            sum += num * num;
        }
        int re = sum % 10;
        bw.write(String.valueOf(re) + "\n");
        bw.flush();
        bw.close();
    }

    public void n2562() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int mx = 0;
        int idx = 0;
        for (int i = 0; i < 9; i++) {
            int num = Integer.parseInt(br.readLine());
            mx = Math.max(mx, num);
            if (mx == num) {
                idx = i;
            }
        }
        bw.write(String.valueOf(mx) + "\n");
        bw.write(String.valueOf(idx + 1) + "\n");
        bw.flush();
        bw.close();
    }

    public void n2577() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int sum = 1;
        for (int i = 0; i < 3; i++) {
            int num = Integer.parseInt(br.readLine());
            sum *= num;
        }
        int[] arr = new int[10];
        while (sum > 0) {
            int rem = sum % 10;
            sum = sum / 10;
            arr[rem] += 1;
        }
        for (int j : arr) {
            bw.write(String.valueOf(j) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public void n2675() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t =  Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String[] inp = br.readLine().split(" ");
            int r = Integer.parseInt(inp[0]);
            char[] carr = inp[1].toCharArray();
            for (char c : carr) {
                for (int j = 0; j < r; j++) {
                    bw.write(c);
                }
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
    
    public void n2739() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n =  Integer.parseInt(br.readLine());
        for (int i = 1; i < 10; i++) {
            bw.write(String.valueOf(n) + " * " + String.valueOf(i));
            bw.write(" = " + String.valueOf(n * i) + "\n");
        }
        bw.flush();
        bw.close();
    }
    
    public void n2741() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n =  Integer.parseInt(br.readLine());
        for (int i = 1; i < n + 1; i++) {
            bw.write(String.valueOf(i) + "\n");
        }
        bw.flush();
        bw.close();
    }
    
    public void n2742() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n =  Integer.parseInt(br.readLine());
        for (int i = n; i > 0; i--) {
            bw.write(String.valueOf(i) + "\n");
        }
        bw.flush();
        bw.close();
    }
    
    public void n2753() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n =  Integer.parseInt(br.readLine());
        if (n % 4 == 0) {
            if (n % 400 == 0) {
                bw.write(1 + "\n");
            } else if (n % 100 == 0) {
                bw.write(0 + "\n");
            } else {
                bw.write(1 + "\n");
            }
        } else {
            bw.write(0 + "\n");
        }
        bw.flush();
        bw.close();
    }

    public void n2884() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int h = Integer.parseInt(arr[0]);
        int m = Integer.parseInt(arr[1]);
        if (m >= 45) {
            bw.write(String.valueOf(h) + " " + String.valueOf(m - 45));
        } else {
            if (h == 0) {
                bw.write("23 " + String.valueOf(m + 15));
            } else {
                bw.write(String.valueOf(h - 1) + " " + String.valueOf(m + 15));
            }
        }
        bw.flush();
        bw.close();
    }
    
    public void n2908() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        char[] a = arr[0].toCharArray();
        char[] b = arr[1].toCharArray();
        char[] ra = new char[a.length];
        char[] rb = new char[b.length];
        for (int i = 0; i < 3; i++) {
            ra[i] = a[2 - i];
            rb[i] = b[2 - i];
        }
        int na = Integer.parseInt(String.valueOf(ra));
        int nb = Integer.parseInt(String.valueOf(rb));
        if (na > nb) {
            bw.write(String.valueOf(na) + "\n");
        } else {
            bw.write(String.valueOf(nb) + "\n");
        }
        bw.flush();
        bw.close();
    }
    
    public void n2920() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int prev = Integer.parseInt(arr[0]);
        int asc = 0;
        int des = 0;
        for (int i = 1; i < 8; i++) {
            int n = Integer.parseInt(arr[i]);
            if (n > prev) {
                asc = 1;
            } else {
                des = 1;
            }
            prev = n;
        }
        if (asc * des != 0) {
            bw.write("mixed\n");
        } else if (asc == 1) {
            bw.write("ascending\n");
        } else {
            bw.write("descending\n");
        }
        
        bw.flush();
        bw.close();
    }
    
    public void n3052() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = new int[42];
        for (int i = 0; i<10; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[num % 42] = 1;
        }
        int sum = 0;
        for (int j : arr) {
            sum += j;
        }
        bw.write(String.valueOf(sum) + "\n");
        bw.flush();
        bw.close();
    }
    
    public void n8958() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            char[] ox = br.readLine().toCharArray();
            int point = 0;
            int sum = 0;
            for (char c : ox) {
                if (c == 'O') {
                    point += 1;
                    sum += point;
                } else {
                    point = 0;
                }
            }
            bw.write(String.valueOf(sum) + "\n");
        }
        bw.flush();
        bw.close();
    }
    
    public void n9498() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        if (t >= 90) {
            bw.write("A\n");
        } else if (t >= 80) {
            bw.write("B\n");
        } else if (t >= 70) {
            bw.write("C\n");
        } else if (t >= 60) {
            bw.write("D\n");
        } else {
            bw.write("F\n");
        }
        bw.flush();
        bw.close();
    }
    
    public void n10171() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("\\    /\\\n");
        bw.write(" )  ( ')\n");
        bw.write("(  /  )\n");
        bw.write(" \\(__)|\n");
        bw.flush();
        bw.close();
    }
    
    public void n10172() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("|\\_/|\n");
        bw.write("|q p|   /}\n");
        bw.write("( 0 )\"\"\"\\\n");
        bw.write("|\"^\"`    |\n");
        bw.write("||_/=\\\\__|\n");
        bw.flush();
        bw.close();
    }
    
    public void n10809() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String arr = br.readLine();
        char[] abc = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        for (char a : abc) {
            int num = arr.indexOf(a);
            bw.write(String.valueOf(num));
            if (a != 'z') {
                bw.write(" ");
            }
        }
        bw.flush();
        bw.close();
    }
    
    public void n10818() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[] inp = br.readLine().split(" ");
        int mx = Integer.parseInt(inp[0]);
        int mn = Integer.parseInt(inp[0]);
        for (int i = 1; i < n; i++) {
            int num = Integer.parseInt(inp[i]);
            if (num > mx) {
                mx = num;
            } 
            if (num < mn) {
                mn = num;
            }
        }
        bw.write(String.valueOf(mn) + " " + String.valueOf(mx) + "\n");
        bw.flush();
        bw.close();
    }
    
    public void n10869() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] inp = br.readLine().split(" ");
        int a = Integer.parseInt(inp[0]);
        int b = Integer.parseInt(inp[1]);
        bw.write(String.valueOf(a + b) + "\n");
        bw.write(String.valueOf(a - b) + "\n");
        bw.write(String.valueOf(a * b) + "\n");
        bw.write(String.valueOf(a / b) + "\n");
        bw.write(String.valueOf(a % b) + "\n");
        bw.flush();
        bw.close();
    }
    
    public void n10871() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] nx = br.readLine().split(" ");
        int n = Integer.parseInt(nx[0]);
        int x = Integer.parseInt(nx[1]);
        int[] arr = new int[n];
        String[] inp = br.readLine().split(" ");
        int i = 0;
        for (String s : inp) {
            int num = Integer.parseInt(s);
            if (num < x) {
                arr[i] = num;
                i += 1;
            }
        }
        for (int j = 0; j < n; j++) {
            if (arr[j] != 0) {
                bw.write(String.valueOf(arr[j]));
                if (j + 1 != n && arr[j + 1] != 0) {
                    bw.write(" ");
                }
            }
        }
        bw.flush();
        bw.close();
    }

    public void n10950() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String[] inp = br.readLine().split(" ");
            int a = Integer.parseInt(inp[0]);
            int b = Integer.parseInt(inp[1]);
            bw.write(String.valueOf(a + b) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public void n10951() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String inp;
        while ((inp=br.readLine()) != null) {
            int a = Integer.parseInt(inp.split(" ")[0]);
            int b = Integer.parseInt(inp.split(" ")[1]);
            bw.write(String.valueOf(a + b) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public void n10952() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String inp;
        while ((inp=br.readLine()) != null) {
            int a = Integer.parseInt(inp.split(" ")[0]);
            int b = Integer.parseInt(inp.split(" ")[1]);
            if (a == 0 && b == 0) {
                break;
            }
            bw.write(String.valueOf(a + b) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public void n10998() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String inp = br.readLine();
        int a = Integer.parseInt(inp.split(" ")[0]);
        int b = Integer.parseInt(inp.split(" ")[1]);
        bw.write(String.valueOf(a * b) + "\n");
        bw.flush();
        bw.close();
    }

    public void n11654() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int inp = br.read();
        bw.write(String.valueOf(inp) + "\n");
        bw.flush();
        bw.close();
    }

    public void n11720() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String a = br.readLine();
        char[] c_arr = br.readLine().toCharArray();
        int sum = 0;
        for (char c : c_arr) {
            sum += c - '0';
        }
        bw.write(String.valueOf(sum) + "\n");
        bw.flush();
        bw.close();
    }
}