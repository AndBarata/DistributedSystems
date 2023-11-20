import java.io.*;
import java.net.*;

public class Target {

	public static void main(String[] args) throws IOException, InterruptedException{

		if(args.length < 1) {
			System.out.println("Usage: java Target <port>");
			System.exit(-1);
		}

		int port = Integer.parseInt(args[0]);
		boolean listening = true;
		ServerSocket server = null;
		Socket socket = null;
		BufferedReader input = null;
		PrintWriter output = null;
		String recv;
		String send = "ACK";

		server = new ServerSocket(port);
		socket = server.accept();
		input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
		output = new PrintWriter(socket.getOutputStream(), true);

		while(listening) {

			recv = input.readLine();
			if(recv != null) {
				System.out.println("Received " + recv);
				if(recv.equals("ping")) {
					output.println(send);
					System.out.println("Sent " + send);
				}
				else {
					System.out.println("Invalid command");
					System.exit(-1);
				}
			}
		}

		input.close();
		output.close();
		socket.close();
		server.close();

	}

}
