import socket

def find_free_port():
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind(('0.0.0.0', 0))  # Bind to any IP and an available port
    port = new_socket.getsockname()[1]
    new_socket.close()
    return port
