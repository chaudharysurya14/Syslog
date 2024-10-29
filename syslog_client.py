import socket

def send_log(message, host='localhost', port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (host, port))
    print(f'Sent: {message}')

if __name__ == "__main__":
    send_log("This is a test log message.")
