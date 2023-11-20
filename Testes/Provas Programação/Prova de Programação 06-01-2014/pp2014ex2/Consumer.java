import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.net.UnknownHostException;

public class Consumer {

	public static void main(String[] args) {
		System.setProperty("java.net.preferIPv4Stack" , "true");

		if(args.length < 2) {
			System.out.println("Usage: <addr> <port>");
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

		MulticastSocket socket = null;
		try {
			socket = new MulticastSocket(port);
			socket.joinGroup(addr);
		} catch (IOException e) {
			System.err.println("Couldn't join group " + addr + " " + port);
			System.exit(-1);
		}
		boolean listening = true;
		byte [] buf = new byte[1024];
		DatagramPacket recv = new DatagramPacket(buf, buf.length);

		while(listening) {
			try {
				socket.receive(recv);
				System.out.println("Received packet: " + new String(recv.getData(), recv.getOffset(), recv.getLength()));
			} catch (IOException e) {
				System.err.println("Couldn't get message");
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
		socket.close();

	}

}
