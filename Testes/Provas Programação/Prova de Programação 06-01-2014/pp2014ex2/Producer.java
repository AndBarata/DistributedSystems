import java.io.IOException;
import java.net.*;

public class Producer {

	public static void main(String[] args) {

		System.setProperty("java.net.preferIPv4Stack" , "true");

		if(args.length < 3) {
			System.out.println("Usage: <addr> <port> <val[1..n]>");
			System.exit(-1);
		}

		InetAddress addr = null;
		try {
			addr = InetAddress.getByName(args[0]);
		} catch (UnknownHostException e) {
			System.err.println("Unknown Host");
			System.exit(-1);
		}
		int port = Integer.parseInt(args[1]);
		int n = args.length - 2;

		MulticastSocket socket = null;
		try {
			socket = new MulticastSocket(port);
			socket.joinGroup(addr);
		} catch (IOException e) {
			System.err.println("Couldn't join group " + addr + " " + port);
			System.exit(-1);
		}
		DatagramPacket dgram;
		for(int i = 2; i < n + 2; i++) {
			dgram = new DatagramPacket(args[i].getBytes(), args[i].length(), addr, port);
			try {
				socket.send(dgram);
				System.out.println("Sent packet: " + new String(dgram.getData(), dgram.getOffset(), dgram.getLength()));
				Thread.sleep(1000); //sleep for 1 second
			} catch (IOException e) {
				System.err.println("Couldn't send message");
				System.exit(-1);
			} catch (InterruptedException e) {
				System.err.println("Error on sleep");
				System.exit(-1);
			}
		}

		try {
			socket.leaveGroup(addr);
			socket.close();
		} catch (IOException e) {
			System.err.println("Couldn't leave group: " + addr + " " + port);
			System.exit(-1);
		}
	}

}
