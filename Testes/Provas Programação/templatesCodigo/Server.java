import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(10000); // Create a server socket on port 5000
            System.out.println("Server is waiting for client request...");

            Socket socket = serverSocket.accept(); // Listen and accept connection from client
            System.out.println("Client connected");

            DataInputStream dataInputStream = new DataInputStream(socket.getInputStream()); // Get input stream
            String message = dataInputStream.readUTF(); // Read message from client
            System.out.println("Message from Client: " + message);

            serverSocket.close(); // Close the server socket
        } catch (IOException e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}