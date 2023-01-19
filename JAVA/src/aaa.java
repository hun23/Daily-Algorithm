import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class aaa {
	public void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// n입력 및 커스텀 클래스 new_stack 생성
		int n = Integer.parseInt(br.readLine());
		new_stack stack = new new_stack(new ArrayList<Integer>());
		for (int i = 0; i < n; i++) {
			// 입력
			String[] inp = br.readLine().split(" ");
			int num = 0;
			// push 경우 처리
			if (inp.length != 1) {
				num = Integer.parseInt(inp[1]);
			}
			String out = do_order(stack, inp[0], num);
			if (!out.isEmpty()) {
				bw.write(out + "\n");
			}
			bw.flush();
		}
		bw.close();
	}

	private String do_order(new_stack stack, String order, int num) {
		int ret = 0;
		if (order == "push") {
			stack.do_push(num);
			return "";
		} else if (order == "size") {
			ret = stack.get_size();
		} else if (order == "empty") {
			ret = stack.is_empty();
		} else if (order == "top") {
			ret = stack.get_top();
		} else if (order == "pop") {
			ret = stack.do_pop();
		}
		return String.valueOf(ret);
	}
}

class new_stack {
	ArrayList<Integer> arr;

	new_stack(ArrayList<Integer> arr) {
		this.arr = arr;
	}

	public int get_size() {
		return arr.size();
	}

	public int is_empty() {
		if (this.get_size() == 0) {
			return 1;
		} else {
			return 0;
		}
	}

	public int get_top() {
		if (this.is_empty() == 1) {
			return -1;
		} else {
			return arr.get(this.get_size() - 1);
		}
	}

	public int do_pop() {
		if (this.is_empty() == 1) {
			return -1;
		} else {
			int temp = arr.get(this.get_size() - 1);
			arr.remove(this.get_size() - 1);
			return temp;
		}
	}

	public void do_push(int num) {
		arr.add(num);
	}
}