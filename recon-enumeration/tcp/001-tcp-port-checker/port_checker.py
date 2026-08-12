import socket
import sys

def check_port(host: str, port: int) -> bool:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(2)

	try:
		sock.connect((host, port))
		return True
	except (ConnectionRefusedError, socket.timeout, OSError):
		return False
	finally:
		sock.close()


if len(sys.argv) != 3:
	print(f"Usage: python {sys.argv[0]} <host> <port>")
	sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

if check_port(host, port):
	print(f"{host}:{port} OPEN")
else:
	print(f"{host}:{port} CLOSED")