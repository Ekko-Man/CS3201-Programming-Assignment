import socket
import sys


def connect_to_server(ser_ip, ser_port):
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (ser_ip, ser_port)
        sock.connect(server_address)
    except:
        print("Connect status: fail")
        sys.exit()
    else:
        print("Connect status: success")
        return sock


def post_to_server(sock):  # handle recive OK
    typing = True
    message = ""

    while typing:  # Loop input text until "."
        line_input = input()
        print(line_input)

        message += line_input + "\n"

        if line_input == ".":
            typing = False

    try:
        sock.sendall(message)  # Send data

        data = sock.recv(1024)
        print("server: ", data)
    except:  # Catch error when the message cant send to server
        print("There are some issue between client and server")


def read_from_server(sock):  # handle data recived from server (print it)
    try:
        message = 'READ'
        sock.sendall(message)  # Send data

        data = sock.recv(1024)
        print("server: ", data)
    except:  # Catch error when the message cant send to server
        print("There are some issue between client and server")


def quit_the_server(sock):  # handle data recived from server (print it)
    try:
        message = 'QUIT'
        sock.sendall(message)  # Send data

        data = sock.recv(1024)
        print("server: ", data)
        sock.close()  # Close the socket connect between client and server.
    except:
        print("There are some issue between client and server, ")


def others_to_server(sock, message):  # handle data recived from server (print it)
    try:
        sock.sendall(message)  # Send data

        data = sock.recv(1024)
        print("server: ", data)
    except:
        print("There are some issue between client and server, ")


if __name__ == '__main__':
    server_port = 16000

    server_ip_port = input("Input the IP address\n")  # 127.0.0.1 16000

    if " " in server_ip_port:
        server_ip, server_port = server_ip_port.split(" ")
    else:
        server_ip = server_ip_port

    print("IP Address: ", server_ip, "\tPort Number: ", server_port)

    sock = connect_to_server(server_ip, server_port)

    socket_connect = True

    while socket_connect:
        input_command = input()
        print("client: ", input_command)

        if input_command == "POST":
            post_to_server(sock)  # read user input and send it to the server.
        elif input_command == "READ":
            read_from_server(sock)  # Send the READ message to server and print out the data.
        elif input_command == "QUIT":
            quit_the_server(sock)
            socket_connect = False
        else:
            others_to_server(sock, input_command)

    sys.exit()
