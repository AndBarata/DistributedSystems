import java.io.*;
import java.net.*;

public class Monitor {

	public static void main(String[] args) throws IOException, UnknownHostException, InterruptedException{

		if(args.length < 4) {
			System.out.println("Usage: java Monitor <addr> <port> <period> <timeout>");
			System.exit(-1);
		}

		Inet4Address addr = (Inet4Address) InetAddress.getByName(args[0]);
		int port = Integer.parseInt(args[1]);
		long period =  Long.parseLong(args[2]);
		int timeout =  Integer.parseInt(args[3]);

		Socket socket = null;
		BufferedReader input = null;
		PrintWriter output = null;
		String recv = null;
		String send = "ping";
		boolean listening = true;

		socket = new Socket(addr, port);
		socket.setSoTimeout(timeout);
		output = new PrintWriter(socket.getOutputStream(), true);
		input = new BufferedReader(new InputStreamReader(socket.getInputStream()));


		while(listening) {

			output.println(send);
			System.out.println("Sent " + send);


			try{
				recv = input.readLine(); //non blocking


			} catch(SocketTimeoutException e){
				System.out.println("Timeout expired, target failed");
				System.exit(-1);
			}catch(IOException e1){
				System.out.println("Timeout expired, target failed");
				System.exit(-1);
			}
			if(recv != null) {
				if(!recv.equals("ACK")) {
					System.out.println("Target responded with invalid command");
					System.exit(-1);
				}
				System.out.println("Received " + recv);
				Thread.sleep(period);
			}
		}

		output.close();
		input.close();
		socket.close();

	}
}
