import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 10000); // Connect to the server on localhost and port 5000

            DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream()); // Get output stream

            dataOutputStream.writeUTF("Hello Server!"); // Send message to server

            socket.close(); // Close the socket
        } catch (IOException e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}
