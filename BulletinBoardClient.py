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
        print("Connect status: : No route to host")
        sys.exit()
    else:
        print("Connect status: success")
        return sock


def post_to_server(sock):  # handle recive OK
    typing = True
    message = ""

    while typing:
        line_input = input()
        print(line_input)

        message += line_input + "\n"

        if line_input == ".":
            typing = False


    try:
        # Send data
        sock.sendall(message)

        data = sock.recv(1024)
        print("server: ", data)
    except:
        print("There are some issue between client and server")


def read_to_server(sock):  # handle data recived from server (print it)
    try:
        # Send data
        message = 'READ'
        sock.sendall(message)

        data = sock.recv(1024)
        print("server: ", data)
    except:
        print("There are some issue between client and server")


if __name__ == '__main__':
    server_port = 16000

    server_ip_port = input("Input the IP address\n")

    if " " in server_ip_port:
        server_ip, server_port = server_ip_port.split(" ")
    else:
        server_ip = server_ip_port

    sock = connect_to_server(server_ip, server_port)

    socket_connect = True

    while socket_connect:
        method_comment = input()
        print("client: ", method_comment)

        if method_comment == "POST":
            read_to_server(sock)    # read user input and send it to the server.
        elif method_comment == "READ":
            read_to_server(sock)    # Send the READ message to server and print out the data.
        elif method_comment == "QUIT":
            sock.close()    # Close the socket connect between client and server.
            socket_connect = False
        else:
            pass

    sys.exit()
