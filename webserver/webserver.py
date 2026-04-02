import socket

def handle_request(client_socket, request_data):
    if "GET /admin" in request_data:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nWelcome to the admin page!"
    else:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, this is a simple web server!"
    
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    # Tạo socket (AF_INET là IPv4, SOCK_STREAM là TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Gắn socket vào địa chỉ IP và Port
    server_socket.bind(('127.0.0.1', 8080))
    
    # Bắt đầu lắng nghe kết nối (tối đa 5 kết nối trong hàng đợi)
    server_socket.listen(5)
    
    print("Server listening on port 8080...")
    
    while True:
        # Chấp nhận kết nối từ client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Nhận dữ liệu yêu cầu (tối đa 1024 bytes)
        request_data = client_socket.recv(1024).decode('utf-8')
        
        # Xử lý yêu cầu thông qua hàm handle_request
        handle_request(client_socket, request_data)

if __name__ == '__main__':
    main()