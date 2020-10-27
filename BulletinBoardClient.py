import socket
import sys


def connect_to_server(ser_ip, ser_port):  # Function to connect to server
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Some socket setting
        sock.settimeout(3)

        server_address = (ser_ip, ser_port)
        sock.connect(server_address)  # Connect to the server
    except Exception as e:  # handle error occur
        print(e)
        sock.close()
        sys.exit()
    else:
        print("Connect status: success")
        return sock


def receive_message(sock):  # Function to receive data from server
    loop_msg = 1
    had_receive_msg = False
    while loop_msg:  # Loop all message send by server
        try:
            data = sock.recv(1024)
            print("server: ", data.decode())
            had_receive_msg = True
            if not data:
                return
        except socket.timeout:
            if had_receive_msg:  # Check normal
                return
            elif not had_receive_msg:  # Handle hanging problem since the server has not sent data back
                print("Socket timeout don't have any message receive from server.")
                sock.close()
                sys.exit()


def post_to_server(sock):  # Handle POST command
    typing = True
    message = "POST\n"

    while typing:  # Loop input text until "."
        line_input = input()
        print("client: ", line_input)
        message += line_input + "\n"
        if line_input == ".":
            typing = False

    try:
        sock.sendall(message.encode())  # Send data
        receive_message(sock)  # Receive and print data from server
    except Exception as e:  # Catch error when the message cant send to server
        print(e)
        sock.close()
        sys.exit()


def read_quit_others_command_to_server(sock, command):  # Handle READ, QUIT, and other not exist command
    message = command.encode()

    try:
        sock.sendall(message)  # Send data
        receive_message(sock)  # Receive and print data from server

        if command == "QUIT":
            sock.close()  # Close the socket connect between client and server.
    except Exception as e:
        print(e)
        sock.close()
        sys.exit()


if __name__ == '__main__':
    server_port = 16000
    server_ip_port = input("Input the IP address\n")  # 127.0.0.1 16000

    if " " in server_ip_port:
        server_ip, server_port = server_ip_port.split(" ")
    else:
        server_ip = server_ip_port

    print("IP Address: ", server_ip, "\tPort Number: ", server_port)
    sock = connect_to_server(str(server_ip), int(server_port))
    socket_connect = True

    while socket_connect:  # Loop handle command from the user until QUIT
        input_command = input()
        print("client: ", input_command)

        if input_command == "POST":
            post_to_server(sock)  # read user input and send it to the server.
        else:
            read_quit_others_command_to_server(sock, input_command)  # Handle READ, QUIT, and other not exist command
            if input_command == "QUIT":  # End the loop when QUIT
                socket_connect = False

    sys.exit()
