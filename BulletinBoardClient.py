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
        return "Connect status: : No route to host"
    else:
        return "Connect status: success"


if __name__ == '__main__':
    server_port = 16000

    server_ip_port = input("Input the IP address\n")

    if " " in server_ip_port:
        server_ip, server_port = server_ip_port.split(" ")
    else:
        server_ip = server_ip_port

    print(connect_to_server(server_ip, server_port))


