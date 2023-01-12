import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class n2557 {
  public void run() throws IOException{
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    bw.write("Hello World!");
    bw.flush();
    bw.close();
  }
}
