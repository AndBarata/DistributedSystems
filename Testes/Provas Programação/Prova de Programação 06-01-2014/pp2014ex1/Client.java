import java.io.*;
import java.net.*;

public class Client {
	private static InetAddress addr;
	private static int port;
	public static void main(String[] args) {
		System.setProperty("preferIPv4Stack", "true");

		if(args.length < 2) {
			System.out.println("Usage: <addr> <port>");
			System.exit(-1);
		}

		try {
			addr = (InetAddress) InetAddress.getByName(args[0]);
		} catch (UnknownHostException e) {
			System.err.println("Unknown Host");
			System.exit(-1);
		}

		port = Integer.parseInt(args[1]);

		Socket socket = null;
		try {
			socket = new Socket(addr, port);
		} catch (IOException e) {
			System.err.println("Could not connect to host " + addr + " on port " + port);
			System.exit(-1);
		}
		DataInputStream input = null;
		PrintWriter output = null;
		try {
			input = new DataInputStream(socket.getInputStream());
		} catch (IOException e) {
			System.err.println("Could not open input stream");
			System.exit(-1);
		}

		try {
			output = new PrintWriter(socket.getOutputStream(), true);
		} catch (IOException e) {
			System.err.println("Could not open output stream");
			System.exit(-1);
		}

		String toSend = new String();
		toSend = "REQUEST";
		output.println(toSend);
		System.out.println("request sent: " + toSend);

		float average;
		//waits for responses
		try {
			while(true) {
				System.out.println("waiting server response");
				average = input.readFloat();
				System.out.println("received response: " + average);
				break;
			}
		} catch (IOException e) {
			System.err.println("Connection failed");
			System.exit(-1);
		}

//		try {
//			socket.close();
//		} catch (IOException e) {
//			System.err.println("Could not close socket");
//			System.exit(-1);
//		}

	}

}
