import socket
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def start_syslog_server(host='0.0.0.0', port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    logging.info(f'Syslog server listening on {host}:{port}')

    while True:
        data, addr = sock.recvfrom(1024)
        logging.info(f'Received message from {addr}: {data.decode()}')

if __name__ == "__main__":
    start_syslog_server()
