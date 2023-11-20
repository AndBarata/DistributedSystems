import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
public class Server {
	private static int port;
	private static float average;
	@SuppressWarnings("resource")
	public static void main(String[] args) {
		System.setProperty("preferIPv4Stack", "true");
		if(args.length < 2) {
			System.out.println("Usage: <port> <average>");
			System.exit(-1);
		}
		port = Integer.parseInt(args[0]);
		average = Float.parseFloat(args[1]);

		ServerSocket server = null;
		Socket socket = null;
		BufferedReader input = null;
		DataOutputStream output = null;
		String rcv = null;
		try {
			server = new ServerSocket(port);
		} catch (IOException e) {
			System.err.println("Could not listen on port: " + port);
			System.exit(-1);
		}
		while(true) {
			try {
				socket = server.accept();
			} catch (IOException e) {
				System.err.println("Accept failed: " + port);
				System.exit(-1);
			}

			try {
				input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			} catch (IOException e) {
				System.err.println("Could not open input stream");
				System.exit(-1);
			}

			try {
				output = new DataOutputStream(socket.getOutputStream());
			} catch (IOException e) {
				System.err.println("Could not open output stream");
				System.exit(-1);
			}


			try {
				rcv = input.readLine(); //blocks
				System.out.println("received request: " + rcv);

			} catch (IOException e) {
				System.err.println("Connection failed");
				System.exit(-1);
			}

			if(rcv.equals("REQUEST")) { //server received valid request
				try {
					output.writeFloat(average);
					output.flush();
				} catch (IOException e) {
					System.err.println("Connection failed");
					System.exit(-1);
				}
				System.out.println("valid request...sent response: " + average);
			}
			else {
				System.out.println("invalid request...discarded");
			}


		}
	}
}
